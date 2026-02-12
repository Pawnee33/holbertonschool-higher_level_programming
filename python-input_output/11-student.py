#!/usr/bin/python3
"""Module that defines a Student class"""


class Student:
    """Defines a student with first name, last name and age"""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary representation of a Student instance"""
        new_dict = {}
        if isinstance(attrs, list):
            for name in attrs:
                if name in self.__dict__:
                    new_dict[name] = self.__dict__[name]
            return new_dict
        return self.__dict__

    def reload_from_json(self, json):
        """
        Updates the Student's attributes from a dictionary.
        Only keys present in the dictionary are changed.
        """
        for key, value in json.items():
            setattr(self, key, value)
