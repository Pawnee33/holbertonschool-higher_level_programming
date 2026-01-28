#!/usr/bin/python3
"""
This module is an empty class Rectangle that define a square
"""


class Rectangle:
    """
    Rectangle define an empty rectangle.
    And have not Attribute yet becauce we want an empty class that define
    rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle with width and height

        Args:
            width and height (int): are the rectangle's side.
            Must be an integer >= 0. Default is 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Method Getter that reads the private attribute __width.

        Returns:
            int the width of private attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Methode Setter that sets the private attribut.
        after checks the validating value.

        Args:
        value : New width of the rectangle.
        Must be an integer ≥ 0.

        Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Method Getter that reads the private attribute __height.

        Returns:
            int the height of private attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Methode Setter that sets the private attribut.
        after checks the validating value.

        Args:
        value : New height of the rectangle.
        Must be an integer ≥ 0.

        Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of the Rectangle.

        Returns:
            int: The area result of width * height.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the Rectangle.

        Returns:
            int: The perimeter result of 2 * (width + height).
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        __str__ returns the rectangle with the character "#".

        Each line contains the number of times the character '#'
        appears horizontally and the number of times it appears vertically.
        If width or height is 0, returns an empty string.
        """
        if self.width == 0 or self.height == 0:
            return ""
        else:
            return (("#" * self.width + "\n") * self.height)[:-1]
