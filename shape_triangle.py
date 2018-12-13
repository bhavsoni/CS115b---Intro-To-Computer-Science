'''
Created on Apr 24, 2012

@author: bribor
'''
from shape import Shape

class Triangle(Shape):
    def __init__(self, x, y, base, height, name="Triangle"):
        super().__init__(x, y, name)
        self.__base = base
        self.__height = height

    @property
    def base(self):
        return self.__base

    @property
    def height(self):
        return self.__height

    @base.setter
    def base(self, base):
        self.__base = base

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def area(self):
        return (self.__base * self.__height) / 2

    def __str__(self):
        return super().__str__() + ", base = " + str(self.__base) + \
            ", height = " + str(self.__height) + ", area = " + str(self.area)

if __name__ == '__main__':
    triangle = Triangle(20, 20, 5, 10)
    print(triangle)
