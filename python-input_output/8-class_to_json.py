#!/usr/bin/python3
"""
This module contains a function that returns the dictionary
description of an object for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object.

    Args:
        obj: An instance of a class.

    Returns:
        dict: The dictionary representation of the object.
    """
    return obj.__dict__
