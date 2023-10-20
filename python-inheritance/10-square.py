#!/usr/bin/python3
"""class Square"""


Rectangle = __import__("9-rectangle").Rectangle


class Square (Rectangle):
    """class Square"""
    def __init__(self, size):
        self.__size = size
        super().__init__(size, size)
        self.integer_validator("size", size)

    def area(self):
        return self.__size * self.__size
