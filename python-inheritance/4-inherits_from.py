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
    
    if type(obj) != a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
