#!/usr/bin/python3
"""
This module is a class Square that define a square.
The class include private attribute __size and checks if size
is an integer >= 0.
"""


class Square:
    """
    Class Square define a square.
    The class has a private attribute to protect the integrity
    of the square.

    Attributes:
        __size : The size of the square's side.
        Size must be an integer >= 0.

    """
    def __init__(self, size=0):
        """
        Initializes a square with a given size.

        Args:
            size (int): The size of the square’s side.
            Must be an integer >= 0. Default is 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Method Getter that reads the private attribut __size.

        Returns:
            int the size of private attribut.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Methode Setter that sets the private attribut.
        after checks the validating value.

        Args:
        value : New size of the square.
        Must be an integer ≥ 0.

        Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area result of __size * __size.
        """
        return self.__size * self.__size
