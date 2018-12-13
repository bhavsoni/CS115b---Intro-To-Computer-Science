'''
Created on May 3, 2013

@author: admin
'''
from circle import Circle
from square import Square
from rectangle import Rectangle
from triangle import Triangle

if __name__ == '__main__':
    list_of_shapes = []
    while True:
        print("Enter the type of shape you wish to create:")
        print("   [C]ircle")
        print("   [T]riangle")
        print("   [R]ectangle")
        print("   [S]quare")
        print("   [Q]uit")
        choice = input("? ").strip().lower()
        if not choice in "ctrsq":
            continue
        if choice == 'q':
            break
        x = int(input("Enter x-coordinate: ").strip())
        y = int(input("Enter y-coordinate: ").strip())
        if choice == 'c':
            radius = float(input("Enter radius: ").strip())
            shape = Circle(x, y, radius)
        elif choice == 't':
            base = float(input("Enter base: ").strip())
            height = float(input("Enter height: ").strip())
            shape = Triangle(x, y, base, height)
        elif choice == 'r':
            length = float(input("Enter length: ").strip())
            width = float(input("Enter width: ").strip())
            shape = Rectangle(x, y, length, width)
        else:
            sidelength = float(input("Enter side length: ").strip())
            shape = Square(x, y, sidelength)
        list_of_shapes.append(shape)
    for shape in list_of_shapes:
        print(shape)