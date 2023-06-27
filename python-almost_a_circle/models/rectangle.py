#!/usr/bin/python3
"""Import statement that inherits from Base (base.py)"""
from models.base import Base


class Rectangle(Base):
    """Determines Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Property for the width of a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter function for private attribute width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Property for the x of a rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter function for private attribute x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Property for the y of a rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter function for private attribute y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns a rectangle's area"""
        return self.__width * self.height

    def display(self):
        """Prints the Rectangle instance with the character '#'"""
        for line in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        """Return representation of string"""
        return "[Rectangle] ({}), {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)
