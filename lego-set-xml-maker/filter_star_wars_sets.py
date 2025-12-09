#!/usr/bin/env python3
import sys
import xml.etree.ElementTree as ET


def load_star_wars_sets(star_wars_xml_path):
    """
    Load Star Wars set numbers from star_wars_sets.xml.
    Extract the portion before '-' (e.g., '7201-1' -> '7201').
    """
    tree = ET.parse(star_wars_xml_path)
    root = tree.getroot()

    star_wars_sets = set()

    for item in root.findall("ITEM"):
        itemid_elem = item.find("ITEMID")
        if itemid_elem is None or not itemid_elem.text:
            continue

        full_itemid = itemid_elem.text.strip()
        base_set_id = full_itemid.split("-", 1)[0]  # before hyphen
        if base_set_id:
            star_wars_sets.add(base_set_id)

    return star_wars_sets


def extract_sets_from_remarks(remarks_text):
    """
    Extract set numbers from a REMARKS string like:
    '41234x3, 75090x1, 65432x2'
    Returns: ['41234', '75090', '65432']
    """
    if not remarks_text:
        return []

    results = []
    parts = remarks_text.split(",")

    for part in parts:
        token = part.strip()
        if not token or "x" not in token:
            continue

        set_number = token.split("x", 1)[0].strip()
        results.append(set_number)

    return results


def main():
    # if len(sys.argv) < 3:
    #    print("Usage: python find_star_wars_sets_in_pieces.py <pieces.xml> <star_wars_sets.xml>")
    #    sys.exit(1)

    pieces_xml_path = "pieces.xml"
    star_wars_xml_path = "star_wars_sets_without_non_existant.xml"

    # Load all Star Wars set numbers
    star_wars_sets = load_star_wars_sets(star_wars_xml_path)
    print(f"Loaded {len(star_wars_sets)} Star Wars sets\n")

    # Parse pieces.xml
    tree = ET.parse(pieces_xml_path)
    root = tree.getroot()

    # Final result: Star Wars sets found inside REMARKS of pieces.xml
    found_sets = set()

    for item in root.findall("ITEM"):
        remarks_elem = item.find("REMARKS")
        if remarks_elem is None or not remarks_elem.text:
            continue

        remarks_text = remarks_elem.text.strip()
        sets_in_remarks = extract_sets_from_remarks(remarks_text)

        # Add any Star Wars sets to the found list
        for s in sets_in_remarks:
            if s in star_wars_sets:
                found_sets.add(s)

    print("Star Wars sets found in pieces.xml REMARKS:")
    for s in sorted(found_sets):
        print(s)

    print(f"\nTotal unique Star Wars sets found: {len(found_sets)}")


if __name__ == "__main__":
    main()