'''
Created on Jan 24, 2017

@author: BhavinSoni
'''
def fahrenheit(celsius):
    """returns the input celsius degrees in fahrenheit."""
    return 9 / 5 * celsius + 32

def celsius(fahrenheit):
    """returns the input fahrenheit degrees in celsius."""
    return 5 / 9 * (fahrenheit - 32)

c = float (input ('enter degrees in celsius: '))
f = fahrenheit(c)

"""print (c,'C= ', f, 'F')"""
print('%.2f c = %.2f F' % (c,f))

f = float (input ('enter degrees in fahrenheit: '))
c= celsius (f)
print (f, 'F=', c, 'C')

"""
try composition of functions.
converting a fahrenheit temperature to 
celsius should give you the original fahrenheit temperature
"""
print () 
f= float (input ('Enter degrees in fahrenheit: '))

assert fahrenheit (celsius(f)) == f
""" use assert to check out the returned value is equal to the expected value
no output should be produced unless the assertion failed 
which mean that you have an error either in your code or expectation """
