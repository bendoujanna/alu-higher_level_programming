#!/usr/bin/python3
"""This module defines a Square with size, position, area, and print."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square with optional size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position with validation."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using '#' based on size and position."""
        if self.__size == 0:
            print()
            return

        # Print vertical offset (new lines)
        for _ in range(self.__position[1]):
            print()

        # Print each row with horizontal offset (spaces)
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
