#!/usr/bin/python3
"""Module: load_json
This module provides a function to load a Python object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Load a Python object from a JSON file.

    Args:
        filename (str): The path to the JSON file.

    Returns:
        object: The Python object represented by the JSON content.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
