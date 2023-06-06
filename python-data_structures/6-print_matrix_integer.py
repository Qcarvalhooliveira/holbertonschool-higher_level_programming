#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for i in line:
            if i != line[-1]:
                print("{:d}".format(i), end=" ")
            else:
                print("{:d}".format(i), end=" ")
        print()
