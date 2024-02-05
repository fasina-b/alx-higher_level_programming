#!/usr/bin/python3
"""Defines a function for checking
if an object is an instance of a specific class."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to check if obj is an instance of.
    Returns:
        True if obj is an instance of a_class, otherwise False.
    """
    return isinstance(obj, a_class)
