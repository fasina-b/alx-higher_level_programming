#!/usr/bin/python3
"""Defines functions for working with JSON files."""

import json


def load_from_json_file(filename):
    """
    Load data from a JSON file and return it as a Python object.

    Args:
        filename (str): The path to the JSON file.

    Returns:
        dict: The Python object representing the JSON data.
    """
    with open(filename) as file:
        return json.load(file)
