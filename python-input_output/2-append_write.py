#!/usr/bin/python3
"""Module that appends a string at the end of a text file (UTF8) and
returns the number of characters added
"""


def append_write(fileneme="", text=""):
    """appends a string at the end of a text file (UTF8) and
    returns the number of characters added
    """
    with open(fileneme, 'a', encoding="utf-8") as f:
        return f.write(text)
