#!/usr/bin/python3
"""
Defines a Student class with basic attributes and
a method to return a dictionary representation.
"""

class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns a dictionary representation of the student instance.
        All attributes are assumed to be serializable.

        Returns:
            dict: The instance's attribute dictionary.
        """
        return self.__dict__
