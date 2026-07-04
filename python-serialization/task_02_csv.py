#!/usr/bin/env python3
"""
This module contains a function that reads data from a CSV file
and converts it into JSON format.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Reads a CSV file and writes its contents to data.json.

    Args:
        csv_filename (str): The name of the CSV file to read.

    Returns:
        bool: True if successful, False if an error occurred.
    """
    try:
        with open(csv_filename, mode="r", encoding="utf-8") as csv_f:
            # Use DictReader to automatically map headers to keys
            reader = csv.DictReader(csv_f)
            data = [row for row in reader]

        with open("data.json", mode="w", encoding="utf-8") as json_f:
            # Serialize the list of dictionaries to JSON
            json.dump(data, json_f, indent=4)

        return True
    except (FileNotFoundError, Exception):
        return False
