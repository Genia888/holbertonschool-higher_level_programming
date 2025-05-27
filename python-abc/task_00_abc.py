#!/usr/bin/python3
"""Abstract Animal class and concrete subclasses using abc"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an Animal"""

    @abstractmethod
    def sound(self):
        """Abstract method to be implemented by all subclasses"""
        pass


class Dog(Animal):
    """Dog class that inherits from Animal"""

    def sound(self):
        return "Bark"


class Cat(Animal):
    """Cat class that inherits from Animal"""

    def sound(self):
        return "Meow"
