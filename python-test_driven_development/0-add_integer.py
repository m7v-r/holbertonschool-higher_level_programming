#!/usr/bin/python3
"""
This is the "0-add_integer" module.
The module provides one function, add_integer(a, b).
For example, add_integer(2, 3) will return 5.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats after casting them to integers.

    Args:
        a: The first number, must be int or float.
        b: The second number, must be int or float. Defaults to 98.

    Returns:
        The sum of a and b as an integer.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
