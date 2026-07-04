#!/usr/bin/python3
"""
This module contains a function that reads a text file
and prints its content to standard output.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
