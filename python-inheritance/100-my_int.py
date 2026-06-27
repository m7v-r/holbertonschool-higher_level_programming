#!/usr/bin/python3
"""
This module defines a class MyInt that inherits from int.
"""


class MyInt(int):
    """
    MyInt is a subclass of int with inverted == and != operators.
    """

    def __eq__(self, other):
        """
        Inverts the behavior of the == operator.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the behavior of the != operator.
        """
        return super().__eq__(other)
