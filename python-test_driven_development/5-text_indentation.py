#!/usr/bin/python3
"""
This module provides the function text_indentation
that prints a text with 2 new lines after each ., ?, or :.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each ., ?, or :.

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()
    if len(text) == 0:
        return

    index = 0
    length = len(text)
    while index < length:
        print(text[index], end="")
        if text[index] in ".?:":
            print("\n\n", end="")
            index += 1
            while index < length and text[index] == " ":
                index += 1
            continue
        index += 1
