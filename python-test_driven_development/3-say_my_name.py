#!/usr/bin/python3
"""
This module provides the function say_my_name
that prints My name is <first name> <last name>.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints: My name is <first name> <last name>.

    Raises:
        TypeError: If first_name is not a string.
        TypeError: If last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if first_name and last_name:
        print(f"My name is {first_name} {last_name}")
    elif first_name and not last_name:
        print(f"My name is {first_name}")
    elif not first_name and last_name:
        print(f"My name is  {last_name}")
    else:
        print("My name is")
