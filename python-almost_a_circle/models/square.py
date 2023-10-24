#!/usr/bin/python3
"""class Square"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """def str"""
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))
