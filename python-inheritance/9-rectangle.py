#!/usr/bin/python3
"""class Rectangle"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle"""
    def __init__(self, width, height):
        super().__init__()
        if self.integer_validator("width", width):
            self.__width = width
        if self.integer_validator("height", height):
            self.__height = height

    def area(self):
        return self.__width * self.__height

    def print(self):
        print ("[Rectangle] {}/{}".format(self.width, self.height))

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.___width, self.__height)
