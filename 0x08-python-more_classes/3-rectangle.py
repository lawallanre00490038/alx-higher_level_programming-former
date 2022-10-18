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

    def area(self):
        """this is a public instance that returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """this is a function that returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """return a eprintable format of the string below"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width 
                    for j in range (self.__height))
        return string
