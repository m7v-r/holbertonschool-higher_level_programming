#!/usr/bin/python3
"""
This module contains a function that returns the JSON
representation of an object (string).
"""
import json


def to_json_string(my_obj):
    """
    Converts a Python object to a JSON string.

    Args:
        my_obj: The object to convert.

    Returns:
        str: The JSON string representation of the object.
    """
    return json.dumps(my_obj)
