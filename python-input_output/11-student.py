#!/usr/bin/python3
"""A class student that defines a student based on 10-student.py"""


class Student:

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

    def reload_from_json(self, json):
        """Replaces all attributes of
           the Student instance with those in json"""
        for key, value in json.items():
            setattr(self, key, value)
