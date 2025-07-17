#!/usr/bin/python3
"""Reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """reads a text file and prints it to stdout

    args:
        filename (str): the name of the file to read.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
