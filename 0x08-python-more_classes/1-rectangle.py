#!/usr/bin/python3
"""
Defines an empty class Rectangle
"""
class Rectangle:
    """Empty representation of a rectangle"""
    def __init__(self, width=0, height=0):
        """This is to initialize width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for the width in the class"""
        return self.__width

    @width.setter
    def width(self, width):
        """the setter of the width inn the class"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """the getter function of the class"""
        return self.__height

    @height.setter
    def height(self, height):
        """the setter function of the class height"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
