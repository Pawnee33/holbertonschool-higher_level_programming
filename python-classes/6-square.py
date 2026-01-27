#!/usr/bin/python3
"""
This module defines a class Square with private
attributes __size and __position,
and checks that size is an integer >= 0
and position is a tuple of 2 positive integers.

"""


class Square:
    """
    Class Square define a square.
    The class has a private attribute to protect the integrity
    of the square.

    Attributes:
        __size : The size of the square's side.
        Size must be an integer >= 0.
        __position (tuple): Tuple of 2
        positive integers for printing offset.

    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square with a given size.

        Args:
            size (int): The size of the square’s side.
            Must be an integer >= 0. Default is 0.
            Position (tuple): Tuple of 2 positive integers for horizontal
            and vertical offset. Default is (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Method Getter that reads the private attribute __size.

        Returns:
            int the size of private attribute.
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

    @property
    def position(self):
        """
        Method Getter that reads the private attribute __position.

        Returns:
            int the position of private attribute.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Methode Setter that sets the private attribut.
        after checks the validating value.
        Position (tuple): Tuple of 2 positive integers
        (horizontal spaces, vertical lines).


        Args:
        value (tuple): New position of the square.
        Must be a tuple of 2 positive integers
        (horizontal spaces, vertical lines).

        Raises:
        TypeError: If value is not a tuple of 2 positive integers.

        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(number, int) for number in value)
            or not all(number >= 0 for number in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area result of __size * __size.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square with the character "#"

        If size is 0, prints an empty line.
        Otherwise, prints a square of '#' characters,
        The square is offset by 'position[0]' spaces horizontally
        and 'position[1]' lines vertically.
        """
        if self.size == 0:
            print("")
        else:
            for _ in range(self.position[1]):
                print("")
            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
