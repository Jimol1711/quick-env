#!/usr/bin/env python3
import sys
import re
import xml.etree.ElementTree as ET


def extract_set_numbers_starting_with_75(remarks_text):
    """
    Extract set numbers from a REMARKS string like:
        "75211x3, 45645x1, 75001x2"
    Only keeps those whose set number starts with "75".
    Returns a list of strings (set numbers only, without 'xQTY').
    """
    results = []

    if not remarks_text:
        return results

    # Example pattern: capture "<SETNUMBER>x<QTY>"
    matches = re.findall(r"([0-9A-Za-z\-]+)x\d+", remarks_text)

    for set_num in matches:
        if set_num.startswith("75"):
            results.append(set_num)

    return results


def main():
    # if len(sys.argv) < 1:
    #    print("Usage: python find_sets_75.py <input_xml>")
    #    sys.exit(1)

    input_xml = "pieces.xml"

    # Parse XML
    tree = ET.parse(input_xml)
    root = tree.getroot()

    found_sets = set()

    # Loop through all ITEM nodes
    for item in root.findall("ITEM"):
        remarks_elem = item.find("REMARKS")
        if remarks_elem is None or not remarks_elem.text:
            continue

        remarks_text = remarks_elem.text.strip()
        extracted = extract_set_numbers_starting_with_75(remarks_text)

        for s in extracted:
            found_sets.add(s)

    # Print results
    print("Sets starting with '75' found in the REMARKS column:")
    for s in sorted(found_sets):
        print(s)


if __name__ == "__main__":
    main()