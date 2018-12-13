# Modify me!

from Shapes import *

if __name__ == '__main__':
    face = Circle(Vector(0, -200), 200, 'yellow')
    face.render()
    left_eye = Circle(Vector(-60, 50), 40, 'black')
    left_eye.render()  
    right_eye = Circle(Vector(60, 50), 40, 'black')
    right_eye.render()
    mouth = Circle(Vector(0, -150), 50, 'red')
    mouth.render()
