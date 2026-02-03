#!/usr/bin/python3
"""
This module returns the list of available attributes and
methods of an object.
"""


def lookup(obj):
    """
    Lookup prints the list of available attributes and
    methods of an object.

    Returns:
        dir: the list of attributes and methods of obj.
    """
    return dir(obj)
