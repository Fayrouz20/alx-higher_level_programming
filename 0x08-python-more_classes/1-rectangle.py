#!/usr/bin/python3

class Rectangle:

    def __init__(self,width=0, height=0):
        self.width = width
        self.height = height
    
    @property
    def width(self):
        return self.__width
    
    def width(self,value):
        if type(value) is not int:
            raise TypeError ("width must be an integer")
        if value < 0 :
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    def height(self,value):
        
        if type(value) is not int:
            raise TypeError ("width must be an integer")
        if value < 0 :
            raise ValueError("width must be >= 0")
        self.__height = value


