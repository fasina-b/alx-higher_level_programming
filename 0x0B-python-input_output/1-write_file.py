#!/usr/bin/python3
"""
Module for writing text to a file.
"""


def write_file(filename="", text=""):
    """
    Writes text to a file.

    Args:
        filename (str): The name of the file.
        text (str): The text to write to the file.

    Raises:
        Exception: If the file cannot be opened.
    """

    with open(filename, 'w', encoding="utf-8") as file:
        file.write(text)
