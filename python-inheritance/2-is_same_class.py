#!/usr/bin/python3
"""
Module that checks obj if it is aninstance of
the specific class.
"""


def is_same_class(obj, a_class):
    """
    is_same_class Method checks if the object is an instance of
    the specific class.

    Rteurns:
        True: if obj is an instance of a_class.
        False: if obj isn't an instance of a_class.
    """
    return type(obj) == a_class
