#!/usr/bin/env python3
"""
This module provides functions to serialize a dictionary to XML
and deserialize an XML file back into a dictionary.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a dictionary into an XML file.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Reads an XML file and returns a deserialized dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        data_dict = {}
        for child in root:
            data_dict[child.tag] = child.text

        return data_dict
    except (FileNotFoundError, ET.ParseError):
        return None
