#!/usr/bin/python3
"""Module that defines BaseGeometry with area and integer validation."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square is a subclass of Rectangle that represents a square
    shape with size as private attributes.
    Size are validated as positive integers.
    """
    def __init__(self, size):
        """
        Initialize a Square instance with size.

        Args:
            Size : size of the square, must be a positive integer.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is <= 0.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
