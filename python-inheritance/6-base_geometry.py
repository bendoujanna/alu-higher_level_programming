#!/usr/bin/python3
"""Base class for geo shapes and raise an exception"""


class BaseGeometry:
    """Base class for geometry shapes."""

    def area(self):
        """Raises an exception for unimplemented area."""
        raise Exception("area() is not implemented")
