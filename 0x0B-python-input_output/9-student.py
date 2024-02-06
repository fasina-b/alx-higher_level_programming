#!/usr/bin/python3
""" Module defining the Student class and its methods.
"""


class Student:
    """ Class representing student instances. """

    def __init__(self, first_name, last_name, age):
        """ Initializes a student with first name, last name, and age. """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Returns a dictionary describing the student. """
        return self.__dict__.copy()
