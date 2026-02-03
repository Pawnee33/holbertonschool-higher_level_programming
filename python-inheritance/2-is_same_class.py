#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    is_same_class checks if the object is instance of
    the specific class.

    Rteurns:
        True: if obj is an instance of a_class.
        False: if obj isn't an instance of a_class.
    """
    if type(obj) == a_class:
        return True
    else:
        return False
