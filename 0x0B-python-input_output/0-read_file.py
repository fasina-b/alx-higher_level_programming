#!/usr/bin/python3
"""
A module containing a function to read text from a file.
"""


def read_file(filename=""):
    """
    Read text from a file and print its contents.

    Args:
        filename (str): The name of the file to read from.

    Raises:
        FileNotFoundError: If the specified file cannot be found.
        PermissionError: specified file cannot be opened permission issues.
    """
    try:
        with open(filename, 'r', encoding="utf-8") as file:
            read_data = file.read()
            print(read_data, end='')
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except PermissionError:
        print(f"Error: Permission denied while trying to open '{filename}'.")
