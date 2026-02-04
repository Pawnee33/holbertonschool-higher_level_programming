#!/usr/bin/python3
"""Module that defines a custom list class with a method to print it sorted."""


class MyList(list):
    """Class that extends list and adds a method to print it sorted."""

    def print_sorted(self):
        """Prints the list sorted in ascending order."""
        print(sorted(self))
