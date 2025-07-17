#!/usr/bin/python3
"""return JSON representation of an obj"""


import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj: The Python object to serialize.

    Returns:
        str: JSON-formatted string.
    """
    return json.dumps(my_obj)
