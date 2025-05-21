#!/usr/bin/python3
# This module defines a Rectangle class with width and height, and includes
# methods to calculate area and perimeter.

class Rectangle:
    """Class that defines a rectangle."""

    def __init__(self, width=0, height=0):
        """
        Initialize the Rectangle with optional width and height.
        Args:
            width (int): rectangle width (default 0)
            height (int): rectangle height (default 0)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method to retrieve the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method to set the width.
        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method to retrieve the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method to set the height.
        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Public method that returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """
        Public method that returns the perimeter of the rectangle.
        If width or height is 0, perimeter is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
