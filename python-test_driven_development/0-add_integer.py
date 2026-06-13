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
        TypeError: If a or b is not an integer, float, or is inf/nan.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Strict check for NaN (NaN is never equal to itself)
    if a != a:
        raise TypeError("a must be an integer")
    if b != b:
        raise TypeError("b must be an integer")

    # Strict check for Infinity / Float Overflow by checking bounds
    if a >= 1e308 or a <= -1e308:
        raise TypeError("a must be an integer")
    if b >= 1e308 or b <= -1e308:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
