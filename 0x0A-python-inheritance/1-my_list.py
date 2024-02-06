#!/usr/bin/python3
"""SortedList module"""


class MyList(list):
    """SortedList class - Inherits from list with added functionality"""

    def print_sorted(self):
        """Prints the list in a sorted order"""
        print(sorted(self))
