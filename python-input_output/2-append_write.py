#!/usr/bin/python3
"""Appends a string at the end of a text file
and return the num of cha added"""


def append_write(filename="", text=""):
    """Apppend a string to the end of a UTF-8 text file
    and return the number cha added

    Creates the file if it does not exist.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
