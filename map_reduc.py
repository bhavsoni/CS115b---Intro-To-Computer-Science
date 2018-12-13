'''
Created on Jan 26, 2017

@author: BhavinSoni
'''
from cs115 import map, reduce, range

def dbl (x):
    return 2*x


def add (x,y):
    return x + y

def span(lst):
    """returns the max and min of the list"""
    return reduce (max,lst) - reduce(min, lst)

def gauss(n):
    """takes in a positve integer n and returns 
    the sum of the first n integers"""
    return reduce(add,range (1, n+1))

def square(x):
    return x*x

def sumofsquares(n):
    """takes integer n and returns the sum of squared n"""
    return reduce(add, map(square, range(1, 1+n)))

lst=[3,4,5]
doubled = map(dbl,lst)
print(doubled)

print (reduce (add, [5,4,3,2,1],0))
print(span([1,2,3,4,90,-1]))

print(gauss(10))
print (sumofsquares(10))
