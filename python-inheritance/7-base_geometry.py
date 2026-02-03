#!/usr/bin/python3
"""
This module is a class BaseGeometry raise an exception if
the area is not implemented
"""


class BaseGeometry:
    """
    BaseGeometry define an empty an geometry.
    And have not Attribute yet becauce we want an empty class that define
    Geometry.
    And raise an exception if the area is not implemented
    """
    def area(self):
        """
        area is a method that raise an exception if the area isn't
        implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer_validator is a method to checks validating value.

        Args:
            name : name of the variable being validated.
            value : the value to validate.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is <= 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
