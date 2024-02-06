#!/usr/bin/python3
"""Defines a function to dynamically add attributes to
objects with a dictionary-based approach."""


def add_attribute(obj, att, value):
    """Dynamically adds a new attribute to an object using a dictionary.

    Args:
        obj (object): The object to which the attribute is to be added.
        att (str): The name of the attribute to add to obj.
        value (any): The value of att.

    Raises:
        TypeError: If the attribute cannot be added due to
        the absence of a dictionary (__dict__).
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    obj.__dict__[att] = value
