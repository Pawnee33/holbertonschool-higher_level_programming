#!/usr/bin/python3
"""Module that prints the object's attributes and
serialize the curent instance of the oject and save
it to the filename
"""
import pickle


class CustomObject:
    """Reprensent a custom object"""
    def __init__(self, name, age, is_student):
        """Initialize an instance with attributes name, age,
        is_student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints out the object's attributes"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current instance of the object
        and save it to the filename
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except (OSError, pickle.PicklingError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize the current instance of the objet
        from the provided filename.
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
