#!/usr/bin/python3
"""
This function adds two integers


"""


def matrix_divided(matrix, div):
    """add_integer function

    """
    if not isinstance(matrix, list) or \
        not all(isinstance(row, list) for row in matrix) or \
        not all(isinstance(element, (int, float)) for row in matrix for element in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise ValueError("Each row of the matrix must have the same size")
    if not isinstance(div, (float, int)):
        raise TypeError ("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
