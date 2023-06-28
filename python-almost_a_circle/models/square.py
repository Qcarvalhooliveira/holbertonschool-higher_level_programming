#!/usr/bin/python3
"""Import statement that inherits from Rectangle(rectangle.py)"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Determines Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return representation of string"""
        return ("[Square] ({}) {}/{} - {}".format(
                    self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """Property for the size of a Square"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter function for public attribute size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns key/value arguments to attributes"""
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]

        for key, value in kwargs.items():
            setattr(self, key, value)
