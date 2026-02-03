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


"""
A subclass module that inherits from BaseGeometry and representing
Rectangle with validated width and height.
"""


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

