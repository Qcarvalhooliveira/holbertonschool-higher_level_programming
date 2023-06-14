#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Constructor"""
        self.size = size
        self.position = position
        """size(int): length of side of the square"""
        """position(int tuple): position of the square"""

    @property
    def size(self):
        """Property for the length of a size of a square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter function for private attribute size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
            """Value: size value to set"""
            """TypeError: if size is not an integer"""
            """ValueError: if size < 0 """
        self.__size = value

    @property
    def position(self):
        """Property for square position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter function for private attribute position"""
        if isinstance(value, tuple) and len(value) == 2:
            if isinstance(value[0], int) and isinstance(value[1], int):
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
            """TypeError: if value is not tuple of 2 positives integers"""

    def area(self):
        """Area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Print the square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
