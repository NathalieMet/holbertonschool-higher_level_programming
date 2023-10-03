#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        line = ' '.join(str(matrix[i][j]) for j in range(len(matrix[i])))
        print(line)
