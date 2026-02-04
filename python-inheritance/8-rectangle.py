#!/usr/bin/python3
"""Module that defines BaseGeometry with area and integer validation."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
