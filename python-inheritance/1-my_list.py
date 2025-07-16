#!/usr/bin/python3
"""Defines class MyList that inherits from list."""


class MyList(list):
    """Custom list class with sorted print method."""

    def print_sorted(self):
        """Prints the list in ascending order."""
        print(sorted(self))
