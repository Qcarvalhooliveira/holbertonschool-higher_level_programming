#!/usr/bin/python3
"""Module for pascal_triangle method"""


def pascal_triangle(n):
    """Returns a list of lists representing Pascal's triangle of n"""
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev_line = triangle[i-1]
        curr_line = [1]
        for j in range(1, i):
            curr_line.append(prev_line[j-1] + prev_line[j])
        curr_line.append(1)
        triangle.append(curr_line)
    return triangle
