#!/usr/bin/python3
"""Module that defines a custom list class with
 a method to print it sorted.
 """


class MyList(list):
    """
    Mylist retrives the behaviour of class list.
    """

    def print_sorted(self):
        """Prints the list in ascending sorted order without modifying it.
        """
        print(sorted(self))
