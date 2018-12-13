'''
Created on Jan 27, 2017

@author: BhavinSoni
'''
from cs115 import map
from math import factorial 
import math

def inverse(n):
    """takes integer n and returns its reciprocal"""
    return 1/n

def e(n):
    list1=range(1,n+1)
    list2=map(factorial,list1) 
    list3=map(inverse,list2)
    answer=sum(list3)+1
    return answer
    """ this function approximates the math e using the Taylor series"""
    """list1 = create the range of values starting from 1 to n+1 depending on the user input"""
    """list2=this takes the input of list1 and applies the math factorial function to it as well as mapping (including) all the terms in that list"""
    """list3=this takes the inverse of the previous list2 and applies the inverse function and then maps (includes) the previous terms """
    """answer=takes the sum of list3. need add +1 because the series starts with 1+...1/(n+1)!"""
    """return= returns approx of the Taylor series function"""

def error (n):
    """returns the absolute value of the difference of the actual math e value and the approx I defined above"""
    return abs(math.e-e(n))
    """returns the absolute value of the actual e value subtracted by the function I defined above (approx of e using Taylor series)"""
