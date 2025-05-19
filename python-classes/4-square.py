#!/usr/bin/python3
"""Defines a class Square with size property and area calculation."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize square with optional size."""
        self.size = size  # Appel du setter -> vérifie & affecte __size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area of the square."""
        return self.__size ** 2
