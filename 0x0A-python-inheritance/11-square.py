#!/usr/bin/python3
"""Square Class Module"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class, inherits from BaseGeometry"""
    def __init__(self, size):
        """Initialize a square with the given size."""
        super().__init__()
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return a string representation of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
