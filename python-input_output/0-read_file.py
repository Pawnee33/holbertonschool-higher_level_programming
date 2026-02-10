#!/usr/bin/python3
"""Module thats read a text file with UTF8"""


def read_file(filename=""):
    """read_file reads a text file with UTF8"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
