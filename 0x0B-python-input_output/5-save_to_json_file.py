#!/usr/bin/python3
"""Defines a function for saving data to a JSON file."""

import json


def save_to_json_file(my_obj, filename):
    """
    Save data to a JSON file.

    Args:
        my_obj: The data to be saved.
        filename (str): The name of the file to save the data to.
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
