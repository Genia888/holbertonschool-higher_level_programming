#!/usr/bin/python3
"""
This module defines the MyList class which extends Python's built-in list.
"""


class MyList(list):

    """A subclass of list that can print sorted version of itself."""

    def print_sorted(self):
        """Prints the list in sorted order."""
        print(sorted(self))
