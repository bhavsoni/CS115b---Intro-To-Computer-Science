'''
Created on Jan 28, 2017

@author: BhavinSoni
'''

from cs115 import map, reduce, range

def mult(x,y):
    return x*y
"""takes 2 numbers and multiples them"""

def factorial(n):
    """takes the n! of a number"""
    return (reduce(mult,range(1,n+1)))
    """applies the multiplication definition to the range of numbers 
    from 1 to the input n and returns n!"""

def add(a,b):
    """returns the sum of 2 numbers"""
    return a+b


def mean (L):
    """takes the average of the list of numbers"""
    return reduce(add,L) / len(L)
    """adds up all the numbers in a list
    and divides it by the number of integers, returning the average"""



def divides (n):
    def div(k):
        return n%k ==0
    return div
"""returns the div functions which determines if integer n is divisible by k and compares the
remainder value to 0. if 0 then true otherwise false"""

def prime(n):
    case1 = range(2,n)
    return sum(map(divides(n), case1)) == 0
"""case1= lists the range of numbers from 2 to n. must be 2 because every integer 
is divisible by 1 and n and so range must be from 2 to n in order to show the remainder value 
is compared to 0. """
"""takes the divides function and maps it to the range defined in case1 and 
takes the sum of it all to convert the integers to true or false"""


print("The facotrial of 7 is " + str(factorial(7)) )