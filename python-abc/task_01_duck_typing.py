#!/usr/bin/python3
"""Abstract base class defining the interface for all shapes"""


from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for all shapes."""

    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Concrete class representing a circle."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (abs(self.radius) ** 2)

    def perimeter(self):
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """Concrete class representing a rectangle."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Duck-typed function to print area
       and perimeter of any shape-like object."""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
