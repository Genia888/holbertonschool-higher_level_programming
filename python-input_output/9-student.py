#!/usr/bin/python3
"""A class that defines a student"""


class Student:

    def __init__(self, first_name, last_name, age):
        """Initializes the student with first name, last name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary representation of the Student instance"""
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
