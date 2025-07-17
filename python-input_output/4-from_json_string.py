#!/usr/bin/python3
"""Returns a Python object represented by a JSON string"""


import json


def from_json_string(my_str):
    """Returns a Python object represented by a JSON string
    Args:
        my_str: A string containing a JSON representation.

    Returns:
        The corresponding Python data structure (list, dict, etc.).
    """
    return json.loads(my_str)
