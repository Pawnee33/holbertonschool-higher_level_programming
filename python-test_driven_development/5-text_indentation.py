#!/usr/bin/python3
"""
Module that provides a function to print text with indentation.

The text_indentation function prints a text and adds two new lines
after each '.', '?' and ':' character.
"""


def text_indentation(text):
    """
    Print a text with two new lines after '.', '?' and ':'.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ".?:"
    index = 0
    length = len(text)

    while index < length:
        char = text[index]
        print(char, end="")
        if char in separators:
            print("\n", end="")
            index += 1
            while index < length and text[index] == " ":
                index += 1
            continue
        index += 1
