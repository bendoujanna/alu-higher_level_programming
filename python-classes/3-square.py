#!/usr/bin/python3
"""adding more features to the previous code"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """
        initializes the square
        Args:
            size(int): the size of the square (default 0)

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates the area of the square

        Returns:
            int: the area of the square
        """
        return self.__size ** 2

