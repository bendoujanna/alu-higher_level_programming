#!/usr/bin/python3
"""
Returns the dictionary description of an object
for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary representation of a simple data object.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: The dictionary form of the object's attributes.
    """
    return obj.__dict__
