#!/usr/bin/python3
"""
That returns True if the object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a specified class."""
    return type(obj) is a_class
