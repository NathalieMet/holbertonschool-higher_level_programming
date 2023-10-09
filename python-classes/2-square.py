#!/usr/bin/python3
"""this is a class for a square"""


class Square:
    """define the features of a square"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
