#!/usr/bin/python3
"""Defines a rectangle with width and height."""


class Rectangle:
    """Defines a rectangle with width and height."""

    number_of_instances = 0  # Tracks number of Rectangle instances
    print_symbol = "#"       # Symbol used for string representation

    def __init__(self, width=0, height=0):
        """Initialize rectangle and increment instance count."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width, must be int >= 0."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height, must be int >= 0."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return area."""
        return self.width * self.height

    def perimeter(self):
        """Return perimeter, or 0 if width or height is 0."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return string with print_symbol or empty string."""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.width
                         for _ in range(self.height)])

    def __repr__(self):
        """Return code-like string to recreate rectangle."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Print message on deletion and decrement instance count."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
