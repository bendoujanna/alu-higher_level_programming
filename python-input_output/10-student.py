#!/usr/bin/python3
"""
Defines a Student class with filtering support in the to_json method.
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

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of a Student instance.
        If attrs is a list of strings, only those attributes will be included.
        Otherwise, all attributes will be returned.
        Args:
            attrs (list or None): List of attribute names to retrieve.
        Returns:
            dict: Dictionary containing selected attributes or all if attrs is None.
        """
        if type(attrs) == list:
            return {k: self.__dict__[k] for k in attrs if k in self.__dict__}
        return self.__dict__
