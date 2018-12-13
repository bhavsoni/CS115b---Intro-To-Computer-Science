'''
Created on Apr 18, 2012

@author: bribor
'''
from abc import ABCMeta, abstractproperty

class Shape(metaclass=ABCMeta):
    def __init__(self, x, y, name="Shape"):
        self.__name = name
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, x):
        self.__x = x

    @y.setter
    def y(self, y):
        self.__y = y

    @abstractproperty
    def area(self):
        pass

    def __str__(self):
        return self.__name + " at (" + str(self.__x) + ", " + str(self.__y) + ")"

if __name__ == '__main__':
    try:
        a = Shape(10, 20)
    except TypeError as error:
        print("Error: " + str(error))
