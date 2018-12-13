'''
Created on Apr 20, 2012

@author: bribor
'''
from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, x, y, length, name="Square"):
        super().__init__(x, y, length, length, name)

    @Rectangle.length.getter
    def length(self):
        return self._Rectangle__length

    @length.setter
    def length(self, length):
        self._Rectangle__length = length
        self._Rectangle__width = length

    @Rectangle.width.getter
    def width(self):
        raise AttributeError("Square has no attribute 'width'.")

    @width.setter
    def width(self, width):
        raise AttributeError("Square has no attribute 'width'.")

if __name__ == '__main__':
    sqr = Square(10, 10, 20)
    sqr.length = 50
    print(sqr)
