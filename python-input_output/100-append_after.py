#!/usr/bin/python3
"""
This module contains a function that inserts a line of text
to a file, after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line containing
    a specific string.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for.
        new_string (str): The string to insert.
    """
    new_data = ""
    with open(filename, mode="r", encoding="utf-8") as f:
        for line in f:
            new_data += line
            if search_string in line:
                new_data += new_string

    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(new_data)
