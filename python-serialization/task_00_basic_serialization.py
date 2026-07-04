#!/usr/bin/env python3
"""
This module provides functionality to serialize a Python dictionary
to a JSON file and deserialize it back into a dictionary.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to a JSON file.
    If the file exists, it is overwritten.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Loads and deserializes data from a JSON file.
    Returns the dictionary representation.
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
