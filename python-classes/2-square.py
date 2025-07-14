#!/usr/bin/python3
"""Write a class Square defines a square"""


class Square:
    """represents a square"""

    def __init__(self, size = 0):
        """
        Initialize the square.

        Args:
            size (int): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an int
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

