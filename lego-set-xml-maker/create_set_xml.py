#!/usr/bin/env python3
import sys
import os
import re
import xml.etree.ElementTree as ET


def parse_remarks(remarks_text):
    """
    Parse a REMARKS string like:
        "41234x3, 45645x1"
    into a dict:
        {"41234": 3, "45645": 1}
    """
    result = {}
    if not remarks_text:
        return result

    # Split by comma
    parts = remarks_text.split(",")
    for part in parts:
        token = part.strip()
        if not token:
            continue

        # Match "<SETNUMBER>x<QTY>"
        m = re.match(r"^([0-9A-Za-z\-]+)x(\d+)$", token)
        if not m:
            # If it doesn't match expected format, ignore that segment
            continue

        set_id = m.group(1)
        qty = int(m.group(2))

        # In case the same set appears more than once, sum quantities
        result[set_id] = result.get(set_id, 0) + qty

    return result


def indent(elem, level=0):
    """
    Pretty-print (indent) an ElementTree in-place.
    """
    i = "\n" + level * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        for child in elem:
            indent(child, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


def filter_xml_by_set(input_path, set_number, output_path=None):
    """
    Read a BrickLink-style wanted list XML file, filter items by REMARKS
    for the given set_number, and write a new XML with only those items.

    - MINQTY will be replaced by the quantity for that specific set.
    - REMARKS will be simplified to "<SETNUMBER>x<qty>" for that item.
    """

    # Parse input XML
    tree = ET.parse(input_path)
    root = tree.getroot()

    # Create new root
    new_root = ET.Element(root.tag)

    # Iterate over all ITEM elements
    for item in root.findall("ITEM"):
        remarks_elem = item.find("REMARKS")
        remarks_text = remarks_elem.text.strip() if remarks_elem is not None and remarks_elem.text else ""

        # Parse REMARKS into {set_number: qty}
        remarks_map = parse_remarks(remarks_text)

        # If this item includes the requested set_number, keep it
        if set_number in remarks_map:
            qty_for_set = remarks_map[set_number]

            if qty_for_set <= 0:
                continue  # ignore zero quantities just in case

            # Clone the ITEM subtree
            new_item = ET.Element("ITEM")
            for child in list(item):
                new_child = ET.SubElement(new_item, child.tag)
                new_child.text = child.text

            # Adjust MINQTY to the quantity for this set
            minqty_elem = new_item.find("MINQTY")
            if minqty_elem is not None:
                minqty_elem.text = str(qty_for_set)

            # Simplify REMARKS to only this set
            new_remarks_elem = new_item.find("REMARKS")
            if new_remarks_elem is not None:
                new_remarks_elem.text = f"{set_number}x{qty_for_set}"

            # Append to new root
            new_root.append(new_item)

    # Pretty-print
    indent(new_root)

    # Decide output path if not given
    if output_path is None:
        base_name = os.path.splitext(os.path.basename(input_path))[0]
        output_path = f"{base_name}_{set_number}.xml"

    # Write result (no XML declaration to keep it BrickLink-friendly)
    new_tree = ET.ElementTree(new_root)
    new_tree.write(output_path, encoding="utf-8", xml_declaration=False)

    return output_path


def main():
    if len(sys.argv) < 3:
        print("Usage: python filter_bricklink_xml_by_set.py <input_xml> <set_number> [output_xml]")
        sys.exit(1)

    input_xml = sys.argv[1]
    set_number = sys.argv[2]

    if len(sys.argv) >= 4:
        output_xml = sys.argv[3]
    else:
        output_xml = None

    output_path = filter_xml_by_set(input_xml, set_number, output_xml)
    print(f"Filtered XML written to: {output_path}")


if __name__ == "__main__":
    main()
