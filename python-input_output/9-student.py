#!/usr/bin/python3
"""
This module defines the Student class.
"""


class Student:
    """
    Representation of a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes the Student instance.

        Args:
            first_name (str): The first name.
            last_name (str): The last name.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
            dict: The dictionary representation.
        """
        return self.__dict__
