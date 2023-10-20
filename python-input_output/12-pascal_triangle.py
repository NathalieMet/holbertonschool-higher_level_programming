#!/usr/bin/python3
"""Pascal's triangle"""


def pascal_triangle(n):
    """Pascal's triangle"""
    triangle = []
    line = [1]
    for j in range(n):
        triangle.append(line)
        next_line = [1]
        for i in range(len(line) - 1):
            next_line.append(line[i] + line[i + 1])
        next_line.append(1)
        line = next_line
    return triangle
