#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math
class Shape(ABC):
    pass
    @abstractmethod
    def area(self):
        """
        Calculate the area of the Shape.

        Returns:
            int: The area result of width * height.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate the perimeter of the Shape.

        Returns:
            int: The perimeter result of 2 * (width + height).
        """
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius
    def area(self):
        """
        Calculate the area of the Shape.

        Returns:
            int: The area result of width * height.
        """
        return math.pi * self.__radius ** 2

    def perimeter(self):
        """
        Calculate the perimeter of the Shape.

        Returns:
            int: The perimeter result of 2 * (width + height).
        """
        return 2 * math.pi * self.__radius

class Rectangle(Shape):
    def __init__(self, width, height):
        """
        Initialize a Rectangle instance with width and height.
        """
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate the area of the Shape.

        Returns:
            int: The area result of width * height.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the Shape.

        Returns:
            int: The perimeter result of 2 * (width + height).
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

def shape_info(obj):
    print("Area:", obj.area())
    print("Perimeter:", obj.perimeter())

