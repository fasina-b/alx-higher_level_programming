#!/usr/bin/python3
"""Customized Integer class module"""


class MyInt(int):
    """A custom Integer class with inverted equality operators"""
    def __eq__(self, other):
        """Overrides and inverts the == operator"""
        return int(self) != int(other)

    def __ne__(self, other):
        """Overrides and inverts the != operator"""
        return int(self) == int(other)
