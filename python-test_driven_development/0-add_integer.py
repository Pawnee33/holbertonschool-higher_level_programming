#!/usr/bin/python3
"""
This module defines a function to add two numbers as integers.
The function checks that both arguments are either integers or floats.
If a float is provided, it is converted to an integer before addition.
Type errors are raised if the arguments are not an integer or float,
or if a float is NaN or infinity.
"""

def add_integer(a, b=98):
    """
    Adds two numbers after converting them to integers if needed.

    Parameters:
        a (int or float): The first number to add.
        b (int or float, optional): The second number to add (default is 98).

    Returns:
        int: The sum of a and b as an integer.

    Raises:
        TypeError: If a or b is not an integer or float,
                   or if a float is NaN or infinity.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float) and (a != a or a == float('inf') or a == float('-inf')):
        raise TypeError("a must be an integer")
    if isinstance(b, float) and (b != b or b == float('inf') or b == float('-inf')):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
