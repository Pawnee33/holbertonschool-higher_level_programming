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
