#!/usr/bin/python3
"""That function returns the dictionary description
   with simple data structure (list, dictionary, string, integer and boolean)
   for JSON serialization of an object."""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure."""
    if hasattr(obj, "__dict__"):
        return obj.__dict__
    else:
        return {}
