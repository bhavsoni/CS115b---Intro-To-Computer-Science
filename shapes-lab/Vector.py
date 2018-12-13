# Vector class

import math

class Vector(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def magnitude(self):
        """ Returns magnitude of vector """
        return math.sqrt(self.x * self.x + self.y* self.y)

    def normalize(self):
        """ Sets vector magnitude to 1 """
        mag = self.magnitude()
        self.x = self.x/mag
        self.y = self.y/mag

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __neg__(self):
        """ This allows us to define a Vector v and then use the notation
        -v to get a new Vector which is the negation of the original! """
        return Vector(-self.x, -self.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        return "Vector: (" + str(self.x) + "," + str(self.y) + ")"

