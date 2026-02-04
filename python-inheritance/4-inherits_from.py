#!/usr/bin/python3
"""
Module that checks if the object is an instance of class
and inherits directly from specified class.
"""


def inherits_from(obj, a_class):
    """
    inherits_from checks if the object is an instance of class
    that inherited 'directly or indirectly' from the specified class
    """

    return False if type(obj) is a_class else issubclass(type(obj), a_class)
