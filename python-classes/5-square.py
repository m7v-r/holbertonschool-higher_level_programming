#!/usr/bin/python3
"""Module that defines a Square class with a print method."""


class Square:
    """Class that represents a square with size and print functionality."""

    def __init__(self, size=0):
        """Initializes the square with a validated size."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the '#' character."""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("#" * self.__size)
