'''
Created on ___3/3/17____________________
@author:   ______Bhavin Soni _________________
Pledge:    _I pledge my honor that I have abided by the Stevens Honor System ______________________

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    if n%2 == 0:
        return False
    return True
        

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    if n == 1:
        return '1'
    elif n%2 == 0:
        return numToBinary(n//2) + '0'
    elif n%2 == 1:
        return numToBinary(n//2) + '1' 

'''print (numToBinary(15))'''

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    elif int(s[0]) == 0:
        return 0 + binaryToNum(s[1:])
    elif int(s[0])  == 1:
        return 2**(len(s)-1) + binaryToNum(s[1:])

print(binaryToNum('10'))

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    if s =='':
        return s
    elif(s[-1]=='0'):
        return s[:-1] + '1'
    else:
        return increment(s[:-1]) + '0'


def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if n == -1:
        return None
    else:
        print (s)
        return count(increment(s), n-1)

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    elif n%3 == 0:
        return numToTernary(n//3) + '0'
    elif n%3 == 1:
        return numToTernary(n//3) + '1'
    else:
        return numToTernary(n//3) + '2'


def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    elif int(s[0]) == 0:
        return 0 + ternaryToNum(s[1:])
    elif int(s[0]) == 1:
        return 1* (3**(len(s)-1)) + ternaryToNum(s[1:])
    elif int(s[0]) == 2:
        return 2* (3**(len(s)-1)) + ternaryToNum(s[1:])
