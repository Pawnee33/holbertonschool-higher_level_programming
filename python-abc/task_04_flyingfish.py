#!/usr/bin/python3
"""
This module demonstrates multiple inheritance in Python.

It defines two parent classes, Fish and Bird, and a child class
FlyingFish that inherits from both. The module illustrates how
method overriding works and how Python handles method resolution
order (MRO) in multiple inheritance.
"""


class Fish:
    """Class representing a fish."""

    def swim(self):
        """Print a message indicating that the fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Print the natural habitat of the fish."""
        print("The fish lives in water")


class Bird:
    """Class representing a bird."""

    def fly(self):
        """Print a message indicating that the bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """Print the natural habitat of the bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Class representing a flying fish.

    Inherits from both Fish and Bird and overrides their methods
    to demonstrate multiple inheritance.
    """

    def fly(self):
        """Print a message indicating that the flying fish is flying."""
        print("The flying fish is soaring!")

    def swim(self):
        """Print a message indicating that the flying fish is swimming."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Print the habitat of the flying fish."""
        print("The flying fish lives both in water and the sky!")
