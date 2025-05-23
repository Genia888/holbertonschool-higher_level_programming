#!/usr/bin/python3
"""
Function that adds two integers
a and are the two integers
Return: a + b
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the result as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
