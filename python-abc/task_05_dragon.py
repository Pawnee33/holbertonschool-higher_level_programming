#!/usr/bin/python3
"""
This module defines a Dragon class using mixins.

It demonstrates how SwimMixin and FlyMixin can be combined
to give a Dragon the ability to swim and fly, showing the
power of modular mixins in Python.
"""


class SwimMixin:
    """Mixin that adds swimming ability to a creature."""
    def swim(self):
        """Prints a message indicating swimming."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that adds flying ability to a creature."""
    def fly(self):
        """Prints a message indicating flying."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A dragon that can both swim and fly."""

    def roar(self):
        """Prints a message indicating the dragon is roaring."""
        print("The dragon roars!")
