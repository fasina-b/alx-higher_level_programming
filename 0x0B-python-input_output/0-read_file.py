#!/usr/bin/python3
"""
Defines a function to read and print the contents of a text file.
"""


def read_file(filename=""):
    """
    Read text from a file and print its contents.

    Args:
        filename (str): The name of the file to read from.

    """
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
