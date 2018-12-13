'''
Created on Apr 20, 2017

@author: BhavinSoni

i pledge my honor that I have abided by the stevens honor system
'''

import math, sys

class QuadraticEquation:
    def __init__(self,a,b,c):
        a = float(a)
        b = float(b)
        c = float(c)

        self.__a = a
        if self.__a == 0:
            raise ValueError("Coefficient 'a' cannot be 0 in a quadratic equation.")
        self.__b = b
        self.__c = c
    
    @property
    def a(self):
        return self.__a
    
    @property
    def b(self):
        return self.__b
    
    @property
    def c(self):
        return self.__c
        
    def discriminant(self):
        return (self.__b ** 2) - (4 * self.__a * self.__c)
    
    def root1(self):
        if self.discriminant() < 0:
            return None
        else:
            return (-self.__b + math.sqrt(self.discriminant()) ) / (2*self.__a)
        
    def root2(self):
        if self.discriminant() < 0:
            return None
        else:
            return (-self.__b - math.sqrt(self.discriminant())) / (2*self.__a)
        
    def __str__(self):
        z = ''
        if self.__a:
            if self.__a == 1:
                z += 'x^2'
            elif self.__a == -1:
                z += '-x^2'
            else:
                z +=  str(self.__a) + 'x^2'
        if self.__b:
            if self.__b == 1:
                z += ' + x'
            elif self.__b == -1:
                z += ' - x'
            elif self.__b > 0:
                z += ' + ' + str(self.__b) + 'x'
            else:
                z += ' - ' + str(abs(self.__b)) + 'x'
        if self.__c:
            if self.__c > 0:
                z += ' + ' + str(self.__c)
            else:
                z += ' - ' + str(abs(self.__c))
        
        z += ' = 0'
        return z
    
if __name__ == '__main__':
    sys.exit(1)
