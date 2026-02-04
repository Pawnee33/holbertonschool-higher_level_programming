#!/usr/bin/python3
"""Module that defines BaseGeometry with area and integer validation."""


class BaseGeometry:
    """Base class for geometry."""

    def area(self):
        """Raises an exception because area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


"""
A subclass module that inherits from BaseGeometry and representing
Rectangle with validated width and height.
"""


class Rectangle(BaseGeometry):
    """
    Rectangle is a subclass of BaseGeometry that represents a rectangle
    shape with width an height as private attributes.
    Width and height are validated as positive integers.
    """
    def __init__(self, width, height):
        """
        Initialize a Rectangle instance with width and height.

        Args:
            width : width of the rectangle, must be a positive integer.
            height : height of the rectangle, must be a positive integer.

        Raises:
            TypeError: if width or height is not an integer.
            ValueError: if width or height is <= 0.
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
