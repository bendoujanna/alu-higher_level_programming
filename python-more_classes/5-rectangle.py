#!/usr/bin/python3
"""detect instance deletion"""


class Rectangle:
    """represents the rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize rectangle with optional width and height (default 0)."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width; must be int >= 0, else raise error."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height; must be int >= 0, else raise error."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area (width * height)."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter; 0 if width or height is 0."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return string of '#' forming the rectangle or empty if 0 size."""
        if self.width == 0 or self.height == 0:
            return ""
        lines = ["#" * self.width for _ in range(self.height)]
        return "\n".join(lines)

    def __repr__(self):
        """Return string to recreate the rectangle via eval()."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Print goodbye message when instance is deleted."""
        print("Bye rectangle...")
