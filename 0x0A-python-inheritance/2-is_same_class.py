#!/usr/bin/python3
"""Module containing is_instance_of_class function"""


def is_same_class(obj, a_class):
    """Check if the given object is an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True: If the object is an instance of the specified class.
        False: Otherwise.
    """
    return type(obj) == a_class
