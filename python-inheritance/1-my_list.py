#!/usr/bin/python3
"""
This module is a class that inherits from list.
"""


class MyList(list):
    """
    Mylist retrives the behaviour of class list.
    """
    def print_sorted(self):
        """
        Print_sorted prints the sort list.
        """
        print(sorted(self))
