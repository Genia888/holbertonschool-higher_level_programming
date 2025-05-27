#!/usr/bin/python3
"""Rectangle module that inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that represents a rectangle, inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initializes a Rectangle with width and height"""
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
