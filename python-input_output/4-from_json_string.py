#!/usr/bin/python3
"""
This module contains a function that returns an object
represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """
    Converts a JSON string to a Python object.

    Args:
        my_str (str): The JSON string.

    Returns:
        object: The Python data structure.
    """
    return json.loads(my_str)
