#!/usr/bin/python3
"""A class that defines a student based on 9-student.py"""


class Student:
    """A class that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes the student with first name, last name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of the Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
