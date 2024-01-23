#!/usr/bin/python3
"""
Module 6-square
Defines a Square class with private attributes size and position,
and public methods area and my_print.
"""


class Square:
    """
    Defines a square with a specified size and position.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square.

        Parameters:
            - size (int): The size of the square.
            - position (tuple): The position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method for size.

        Returns:
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for size.

        Parameters:
            - value (int): The size of the square.

        Raises:
            - TypeError: If size is not an integer.
            - ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter method for position.

        Returns:
            The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for position.

        Parameters:
            - value (tuple): The position of the square.

        Raises:
            - TypeError: If position is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(i, int) for i in value) or \
                not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using '#' characters.
        Takes into account the position attribute.
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
