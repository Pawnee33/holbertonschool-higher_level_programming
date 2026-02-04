#!/usr/bin/python3
"""Module that defines BaseGeometry with area and integer validation."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry



class Rectangle(BaseGeometry):
    """
    Rectangle is a subclass of BaseGeometry that represents a rectangle
    shape with width and height as private attributes.
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
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate the area of the Rectangle.

        Returns:
            int: The area result of width * height.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return the string representation of the Rectangle in the format:
        [Rectangle] <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


"""
A subclass module that inherits from BaseGeometry and representing
square with validated size.
"""


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
