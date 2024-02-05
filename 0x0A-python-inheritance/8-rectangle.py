#!/usr/bin/python3
"""
Defines a Rectangle class that inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

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
