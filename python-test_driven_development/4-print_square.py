#!/usr/bin/python3


def print_square(size):
    """ Prints square

        Raises:
            TypeError: size must be an integer
            TypeError: size must be >= 0
            TypeError: size must be an integer
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    if isinstance(size, float) and size <= 0:
        raise TypeError("size must be an integer")
    for item in range(0, size):
        print("#" * size)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
