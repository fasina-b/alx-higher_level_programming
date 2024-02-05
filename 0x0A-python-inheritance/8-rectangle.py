#!/usr/bin/python3
"""
Defines a Rectangle class that inherits from BaseGeometry.
"""

from 7-base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle and inherits from the BaseGeometry class.
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
