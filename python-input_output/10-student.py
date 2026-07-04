#!/usr/bin/python3
"""
This module defines the Student class with attribute filtering.
"""


class Student:
    """
    Representation of a student with filtering capabilities.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes the Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): List of attribute names to retrieve.

        Returns:
            dict: The dictionary representation.
        """
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            return {
                key: getattr(self, key) for key in attrs if hasattr(self, key)
            }
        return self.__dict__
