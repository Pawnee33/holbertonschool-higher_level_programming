#!/usr/bin/env python3
"""
This module defines abstract and concrete shapes (Circle, Rectangle)
and a function `shape_info` to display their area and perimeter.

Classes:
    Shape: Abstract base class defining the interface for shapes.
    Circle: Concrete class representing a circle, inherits from Shape.
    Rectangle: Concrete class representing a rectangle, inherits from Shape.

Functions:
    shape_info(obj): Prints the area and perimeter of any shape
    object implementing the area() and perimeter() methods
    (uses duck typing).
"""
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class for all shapes.

    Any shape must implement the `area` and `perimeter` methods.
    """

    @abstractmethod
    def area(self):
        """
        Calculate the area of the Shape.

        Returns:
            float: The area result of Shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate the perimeter of the Shape.

        Returns:
            float: The perimeter result of Shape.
        """
        pass


class Circle(Shape):
    """Circle shape defined by its radius."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """
        Calculate the area of the Shape.

        Returns:
            float: The area result of pi * radius ** 2.
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Calculate the perimeter of the Shape.

        Returns:
            float: Perimeter of the circle using 2 * math.pi * radius.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle shape defined by width and height."""

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance with width and height.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate the area of the Shape.

        Returns:
            float: The area result of width * height.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the Shape.

        Returns:
            float: The perimeter result of 2 * (width + height).
        """
        return 2 * (self.width + self.height)


def shape_info(obj):
    """Print the area and perimeter of any shape.

    Uses duck typing: the object must have `area` and `perimeter` methods.

    Args:
        obj (Shape): An instance of a shape.
    """
    print("Area:", obj.area())
    print("Perimeter:", obj.perimeter())
