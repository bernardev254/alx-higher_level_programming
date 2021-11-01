#!/usr/bin/python3
"""module definging a square class and prints a square"""


class Square:
    """Private instance attribute: size
    Instantiation with optional size: def __init__(self, size=0):
    size must be an integer, otherwise raise a TypeError
    exception with the message size must be an integer
    if size is less than 0, raise a ValueError exception
    with the message size must be >= 0
    """
    def __init__(self, size=0, position=(0, 0)):
        """data initialization
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """retrives the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets size to value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """gets the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets position to value"""
        if not isinstance (value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns area of the square"""
        return self.__size ** 2

    def my_print(self):
        """prints the square"""
        if self.__size == 0:
            print()
        else:
            for a in range(0, self.__size):
                for b in range(0, self.__size):
                    for i in range(0, self.__position[0]):
                            print("", end="")
                    print("#", end="")
                print()
