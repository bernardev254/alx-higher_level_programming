#!/usr/bin/python3
class Square:
    """Private instance attribute: size
    Instantiation with optional size: def __init__(self, size=0):
    size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
    if size is less than 0, raise a ValueError exception with the message size must be >= 0
    """
    def __init__(self, size = 0):
        """data initialization
        """
        self.__size = size

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

    def area(self):
        """Returns area of the square"""
        return self.__size ** 2
