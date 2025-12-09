#!/usr/bin/env python3
import sys
import xml.etree.ElementTree as ET


EXCLUDED_ITEMS = {
    "30727", "5001167", "5002512", "5002513", "5002514", "5004243",
    "5008118", "6476267", "6523825", "6523826", "6556842", "65828",
    "66142", "66150", "66808", "75090", "75436", "75437", "75440",
    "75441", "75443", "75448", "75449", "75452", "EG00126", "EG00132",
    "LUKE", "MAY2013", "MAZKANATA", "PORG", "promosw006", "TIEFIGHTER",
    "TOYFAIR2005", "TOYFAIR2011", "TRUGhost", "TRUSWMF", "TRUWOOKIE",
    "TRUXWING", "XWING"
}


def indent(elem, level=0):
    """Pretty XML indentation."""
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


def filter_xml(input_path, output_path):
    tree = ET.parse(input_path)
    root = tree.getroot()

    new_root = ET.Element("INVENTORY")

    for item in root.findall("ITEM"):
        itemid_elem = item.find("ITEMID")
        if itemid_elem is None or not itemid_elem.text:
            continue

        full_itemid = itemid_elem.text.strip()
        base_itemid = full_itemid.split("-", 1)[0]  # before "-"

        # Only keep items NOT in the exclusion list
        if base_itemid not in EXCLUDED_ITEMS:
            new_root.append(item)

    indent(new_root)
    new_tree = ET.ElementTree(new_root)
    new_tree.write(output_path, encoding="utf-8", xml_declaration=False)


def main():
    # if len(sys.argv) < 3:
    #    print("Usage: python remove_nonexistant_star_wars_sets.py <input_xml> <output_xml>")
    #    sys.exit(1)

    input_xml = "star_wars_sets.xml"
    output_xml = "star_wars_sets_without_non_existant.xml"

    filter_xml(input_xml, output_xml)
    print(f"Filtered XML written to: {output_xml}")


if __name__ == "__main__":
    main()