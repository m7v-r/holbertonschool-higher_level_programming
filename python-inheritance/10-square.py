#!/usr/bin/python3
"""
This module defines a class Square that inherits from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class that represents a square, inheriting from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes the square with size.

        Args:
            size (int): The size of the square's sides.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
