#!/usr/bin/python3
"""
This module defines a CountedIterator class that keeps track
of the number of items iterated over.
"""


class CountedIterator:
    """
    CountedIterator wraps an iterator and counts how many items
    have been fetched from it.
    """

    def __init__(self, iterable):
        """
        Initialize the iterator and the counter.
        """
        self.iterator = iter(iterable)
        self.counter = 0

    def get_count(self):
        """
        Return the number of items that have been iterated over.
        """
        return self.counter

    def __next__(self):
        """
        Return the next item from the iterator and increment the counter.
        """
        item = next(self.iterator)
        self.counter += 1
        return item
