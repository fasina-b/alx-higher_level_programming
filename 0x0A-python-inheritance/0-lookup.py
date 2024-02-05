#!/usr/bin/python3
"""Defines a function to retrieve
a list of attributes from an object."""


def lookup(obj):
    """Return a list of attributes
    available in the given object."""
    return dir(obj)
