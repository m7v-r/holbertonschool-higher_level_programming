#!/usr/bin/python3
"""
This module defines a BaseGeometry class with an unimplemented area method.
"""


class BaseGeometry:
    """
    A class with a public method area.
    """

    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")
