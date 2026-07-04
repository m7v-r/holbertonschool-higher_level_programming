#!/usr/bin/python3
"""
This module contains a function that creates an Object
from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        object: The Python object created from the file.
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
