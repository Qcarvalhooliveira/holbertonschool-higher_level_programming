#!/usr/bin/python3
"""Function that write a class Rectangle that defines a rectangle """


class Rectangle:
    """Defines rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Constructor"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
        """width: width of side of the rectangle"""
        """height: height of the rectangle"""

    @property
    def width(self):
        """Property for the width of a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter function for private attribute width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
            """Value: widht value to set"""
            """TypeError: if width is not an integer"""
            """ValueError: if width < 0 """
        self.__width = value

    @property
    def height(self):
        """Property for the height of a rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter function for private attribute height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
            """Value: height value to set"""
            """TypeError: if width is not an integer"""
            """ValueError: if width < 0 """
        self.__height = value

    def area(self):
        """Returns a rectangle's area"""
        return self.__width * self.height

    def perimeter(self):
        """Returns a rectangle's perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """Returns string representation"""
        string = ""
        if self.width == 0 or self.height == 0:
            return string
        for i in range(self.height):
            string += str(self.print_symbol) * self.width + '\n'
        return string[:-1]

    def __repr__(self):
        """Representation"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """delete"""
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
