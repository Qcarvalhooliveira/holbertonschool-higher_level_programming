#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new_matrix = []
    for line in matrix:
        new_line = []
        for element in line:
            new_line.append(element ** 2)
        new_matrix.append(new_line)
    return (new_matrix)
