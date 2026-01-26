#!/usr/bin/python3
"""
This module is a class Square that define a square.
Class include private attribute __size and checks if size
is an integer >= 0.
"""


class Square:
    """
    Class Square define a square.
    The class has a private attribute to protect the integrity
    of the square.

    Attributes:
        Private attribute __size : Description of size.
        size must be an integer >= 0.

    """
    def __init__(self, size=0):
        """
        Initialises asquare with a given size.

        Args:
            size: The size of the square's side. Must be >= 0.
                Defaul is 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
