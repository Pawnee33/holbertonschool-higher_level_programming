#!/usr/bin/python3
"""
Module that provides a function to print text with indentation.

The text_indentation function prints a text and adds two new lines
after each '.', '?' and ':' character.
"""


def text_indentation(text):
    """
    Print a text with two new lines after '.', '?' and ':'.

    text must be a string, otherwise a TypeError is raised.
    No line should start or end with a space.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ".?:"
    index = 0

    while index < len(text):
        print(text[index], end="")

        if text[index] in separators:
            print("\n", end="")
            index += 1
            while index < len(text) and text[index] == " ":
                index += 1
            continue

        index += 1