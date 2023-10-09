#!/usr/bin/python3
"""
This function adds two integers


"""


def add_integer(a, b=98):
    """add_integer function

    """
    if a is None or (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return (a + b)
