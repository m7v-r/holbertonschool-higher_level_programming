#!/usr/bin/python3
"""
This is the "5-text_indentation" module.
The module provides one function, text_indentation(text).
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text: The input string to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Clean character-by-character printing logic without trailing text issues
    skip_space = True
    for char in text:
        if skip_space and char == ' ':
            continue
        skip_space = False
        print(char, end="")
        if char in ['.', '?', ':']:
            print("\n")
            skip_space = True
