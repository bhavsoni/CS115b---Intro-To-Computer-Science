'''
Created on Mar 23, 2017

@author: BhavinSoni
'''
import sys

def divide(x,y):
    if not isinstance(x, int) and not isinstance(x,float):
        raise TypeError(str(x) + ' is not a number')
    if y == 0:
        raise ZeroDivisionError('Cannot divide ' + str(x) + ' by 0.')
    return x / y

def get_string(prompt):
    s = input(prompt)
    if len(s) > 10:
        raise ValueError('string exceeds max length of 10 characters')
    return s


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
            print('You did not enter a valid integer')
    

#age = get_int('Enter your age: ')
#print('You are %d years old.' % age)

try:
    name = get_string('Enter your name: ')
    age = get_int('enter your age: ')
except ValueError as error:
    print ('Error:' , error)
    sys.exit(1)
    '''1 means its a failure'''


try:            
    print(divide(len(name),2))
    print('You are %d years old.' % age)
except (ZeroDivisionError, TypeError) as error:
    print('Error: ' , error)
sys.exit(0)
'''0 is a success'''