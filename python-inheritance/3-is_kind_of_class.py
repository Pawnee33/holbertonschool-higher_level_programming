#!/usr/bin/python3
"""
Module that checks obj if it's come tospecific class
"""


def is_kind_of_class(obj, a_class):
    """
    is_kind_of_class is method that checks if obj come of
    a specific class exactly or an inherited class.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
