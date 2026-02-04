#!/usr/bin/python3
"""
This module is a class that inherits from list.
"""


class MyList(list):
    """
    Mylist retrives the behaviour of class list.
    """

    def print_sorted(self):
        """Prints the list in ascending sorted order without modifying it.
        """
        print(sorted(self))
