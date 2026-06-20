#!/usr/bin/python3
"""Module that defines a Square class with rich comparison methods."""


class Square:
    """Class that represents a square with size and comparison logic."""

    def __init__(self, size=0):
        """Initializes the square with a validated size."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validation (float or int)."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square."""
        return self.__size * self.__size

    def __eq__(self, other):
        """Check if area is equal."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if area is not equal."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if area is less than."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if area is less than or equal to."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if area is greater than."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if area is greater than or equal to."""
        return self.area() >= other.area()
