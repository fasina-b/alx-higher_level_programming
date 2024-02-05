#!/usr/bin/python3
"""Defines a base geometry class with
an unimplemented area method."""


class BaseGeometry:
    """Represent a basic geometric shape."""

    def area(self):
        """Calculate the area of the geometric shape (not implemented)."""
        raise Exception("area() is not implemented")
