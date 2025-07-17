#!/usr/bin/python3
"""
Script: 7-add_item.py

This script adds all command-line arguments to a Python list
and saves them to a file named `add_item.json` using JSON representation.

It uses two helper functions:
- `save_to_json_file`: from 5-save_to_json_file.py
- `load_from_json_file`: from 6-load_from_json_file.py

If the file doesn't exist, it is created.
"""

import sys
import os

# Importing functions from previous tasks
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Load the existing list if the file exists
if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Extend the list with command-line arguments
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)
