# !/usr/bin/env python3

# Take an XML file, have the user specify an element containing
# a base64-encoded string and return a text file with the decoded string written into it.
# The script assumes the XML file is contained in the same directory as itself.

import os
import base64
import xml.etree.ElementTree as ET


def decode_base64(encoded_string):
    decoded_bytes = base64.b64decode(encoded_string)
    return decoded_bytes.decode("UTF-8")


def process_xml(file_name):
    # Load the XML file
    tree = ET.parse(file_name)
    root = tree.getroot()

    # Find the specified element
    element = root.find(element_name)
    if element is None:
        print("Element not found in the XML file.")
        return

    # Decode the base64-encoded string
    encoded_string = element.text
    decoded_string = decode_base64(encoded_string)

    # Write the decoded string into a text file
    output_file = "decoded_text.txt"
    with open(output_file, "w") as file:
        file.write(decoded_string)

    print("Decoded string has been written to", output_file)


# Get the directory of the code file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Iterate through the directory's files to find the XML one
xml_files = [file for file in os.listdir(current_dir) if file.endswith(".xml")]

if not xml_files:
    print("No XML file found in the current directory.")
elif len(xml_files) > 1:
    print("More than one XML file were found.")
else:
    # Pick out the file as an item from the list
    xml_file = xml_files[0]

    # Get the element name from the user
    element_name = input("Enter the name of the XML element containing the encoded string: ")

    # Process the XML file
    xml_path = os.path.join(current_dir, xml_file)
    process_xml(xml_path)