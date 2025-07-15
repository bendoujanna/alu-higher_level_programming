#!/usr/bin/python3
"""This module defines a Square with size, area, and print functionality."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """
        Initializes the square.

        Args:
            size (int): The size of the square (default is 0).

        """
        self.__size = size

    @property
    def size(self):
        """retrieves the size of the square
        returns:
            int: the current size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size of the square with validation.
         Args:
            value (int): The new size value.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """prints the square with the character #
        if size == 0, print an empty line
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
