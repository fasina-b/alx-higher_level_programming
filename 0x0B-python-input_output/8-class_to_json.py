#!/usr/bin/python3
"""Defines a function to convert a
Python class instance to a JSON-compatible dictionary."""


def class_to_json(obj):
    """Converts a Python class instance
    to a dictionary representation."""
    return obj.__dict__
