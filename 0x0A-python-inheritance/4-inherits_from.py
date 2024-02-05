#!/usr/bin/python3
"""Module containing inherits_from method"""


def inherits_from(obj, a_class):
    """
    Checks if the given object is an instance
    of a class that directly or indirectly
    inherits from the specified superclass.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if obj is an instance of a subclass
        (directly or indirectly) of superclass, otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
