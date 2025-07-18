#!/usr/bin/python3
"""
This module defines a Student class with methods
to serialize and deserialize student instances.
"""


class Student:
    """
    Defines a student with first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the student.

        Args:
            attrs (list, optional): List of attribute names to include.
                                     If not a list, returns all attributes.

        Returns:
            dict: A dictionary of attributes.
        """
        if isinstance(attrs, list) and all(isinstance(e, str) for e in attrs):
            return {k: self.__dict__[k] for k in attrs if k in self.__dict__}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the student using a dictionary.

        Args:
            json (dict): A dictionary of new attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
