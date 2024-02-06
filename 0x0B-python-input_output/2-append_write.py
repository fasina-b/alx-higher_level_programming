#!/usr/bin/python3
"""Defines a function to append text to a file."""


def append_write(filename="", text=""):
    """Appends text to the end of a UTF-8 encoded file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
