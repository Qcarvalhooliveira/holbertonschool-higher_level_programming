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
        return ("[Square] ({}), {}/{} - {}".format(
            self.id, self.x, self.y, self.width))
