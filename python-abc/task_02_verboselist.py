#!/usr/bin/python3
"""
This module defines a VerboseList class that extends the built-in list
and prints notification messages whenever the list is modified.
"""


class VerboseList(list):
    """
    VerboseList extends the built-in list class and prints messages
    whenever elements are added or removed.
    """

    def append(self, item):
        """
        Add an item to the list and print a notification message.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, x):
        """
        Extend the list with multiple items and print a notification message.
        """
        super().extend(x)
        print(f"Extended the list with [{len(x)}] items.")

    def remove(self, item):
        """
        Remove the first occurrence of an item from the list
        and print a notification message.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Remove and return an item from the list at the given index
        and print a notification message.
        """
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
