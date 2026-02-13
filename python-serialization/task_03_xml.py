#!/usr/bin/python3
"""
XML serialization module.

Provides functions to write a dictionary to XML and read it back.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Write a dictionary to an XML file.

    Args:
        dictionary (dict): Data to serialize.
        filename (str): Output XML file.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    ET.indent(root, space="    ")

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Read an XML file and return a dictionary.

    Args:
        filename (str): Input XML file.

    Returns:
        dict: Deserialized data.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    data = {child.tag: child.text for child in root}
    return data
