# Shape classes
# Last modified on April 22, 2016

import math
import turtle

from Matrix import *
from Vector import *

class Shape(object):
    def __init__(self):
        self.points = []
        
    def render(self):
        """Use turtle graphics to render shape"""
        turtle.penup()
        turtle.setposition(self.points[0].x, self.points[0].y)
        turtle.pendown()
        turtle.fillcolor(self.color)
        turtle.pencolor(self.color)
        turtle.begin_fill()
        for vector in self.points[1:]:
            turtle.setposition(vector.x, vector.y)
        turtle.setposition(self.points[0].x, self.points[0].y)
        turtle.end_fill()

    def erase(self):
        """Draw shape in white to effectively erase it from screen"""
        temp = self.color
        self.color = "white"
        self.render()
        self.color = temp
    
    def rotate(self, theta):
        """Rotate shape by theta degrees """
        theta = math.radians(theta)  # THIS IS CORRECT!
        # Python's trig functions expect input in radians
        # so this function converts from degrees into radians.
        RotationMatrix = Matrix(math.cos(theta), -1*math.sin(theta), math.sin(theta), math.cos(theta))
        NewPoints = []
        for vector in self.points:
            newvector = RotationMatrix * vector
            NewPoints.append(newvector)
        self.points = NewPoints
        
    
    def translate(v = vector(0,0)):
        x = self.x
        y = self.y
        turtle.setposition()
        
class Rectangle(Shape):
    def __init__(self, width, height, center = Vector(0, 0), color = "black"):
        SW = Vector(center.x - width/2.0, center.y - height/2.0)
        NW = Vector(center.x - width/2.0, center.y + height/2.0)
        NE = Vector(center.x + width/2.0, center.y + height/2.0)
        SE = Vector(center.x + width/2.0, center.y - height/2.0)
        self.points = [SW, NW, NE, SE]
        self.color = color

class Square(Rectangle):
    def __init__(self, width, center=Vector(0, 0), color = "black"):
        super().__init__(width, width, center, color)
        
class Circle(Shape):
    def __init__(self, center = Vector(0, 0), radius = 10, color = "black"):
        self.center = center
        self.radius = radius
        self.color = color

    def render(self):
        turtle.penup()
        turtle.setposition(self.center.x, (self.center.y - self.radius))
        turtle.pendown()
        turtle.fillcolor(self.color)
        turtle.pencolor(self.color)
        turtle.begin_fill()
        turtle.circle(self.radius)
        turtle.end_fill()

    def rotate(self, theta):
        """ theta is in degrees """
        theta = math.radians(theta)
        RotationMatrix = Matrix(math.cos(theta), -1*math.sin(theta), math.sin(theta), math.cos(theta))        
        self.center = RotationMatrix * self.center
        
class Triangle(Shape):
    def __init__(self, length = 5, height=10, center=Vector(0,0), color = "blue"):
        self.length
        self.height
        self.center
        self.color
        
        
