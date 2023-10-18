#!/usr/bin/python3
""" class MyList that inherits from list"""


class MyList(list):
    """ My custom list class
    """
    def print_sorted(self):
        for element in self:
            if not isinstance(element, int):
                raise TypeError('All elements must be integers')
        print (sorted(self))
