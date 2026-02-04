#!/usr/bin/python3
"""
Module that checks obj if it is aninstance of
the specific class.
"""


def is_same_class(obj, a_class):
    """
    Method checks if the object is an instance of
    the specific classand return True.
    """

    return type(obj) is a_class
