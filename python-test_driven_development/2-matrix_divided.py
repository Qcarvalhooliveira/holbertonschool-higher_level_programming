#!/usr/bin/python3


def matrix_divided(matrix, div):
    """
        Divides all elements of a matrix by div.

        Args:
            matrix: list of list containing int/floats.
            div: number to divide matrix

        Returns:
            new matrix

        Raises:
            TypeError: if matrix is not a list of the lists
            TypeError: if rows are not the same size
            TypeError: if div is neither int nor float
            ZeroDivisionError: when div is zero
     """

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []

    for row in matrix:
        new_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_element = round(element / div, 2)
            new_row.append(new_element)
        new_matrix.append(new_row)

    return new_matrix

    if __name__ == "__main__":
        import doctest
            doctest.testfile("tests/2-matrix_divided.txt")
