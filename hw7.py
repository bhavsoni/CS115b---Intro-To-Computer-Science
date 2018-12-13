'''
Created on Mar 21, 2017

@author: BhavinSoni

PLedge: I pledge my honor that I have abided by the Stevens Honor System
'''

def numToBaseB (N, B):
    '''takes as input a non-negative (0 or larger) integer N and a 
    base B (between 2 and 10 inclusive) and returns a string representing the number N in base B.'''
    if N == 0:
        return ''
        '''if integer N is 0 then return empty string'''
    elif N % B == 0:
        return numToBaseB(N//B , B) + '0'
        '''if the remainder between the division of N and B is 0, the fuction is called
        recursively but N and B are divided (not true division) and a 0 is added'''
    else:
        return numToBaseB(N//B , B) + '1'
        '''if the remainder between the division between N and B is not 0, the function 
        is recursively recalled but N and B are divided (not true division) and a 1 is added'''

print(numToBaseB(15,10))

def baseBToNum (S, B):
    '''takes as input a string S and a base B where S represents a number in 
    base B where B is between 2 and 10 inclusive. Returns an integer in base 
    10 representing the same number as S'''
    if S == '':
        return 0
        '''if the string S is empty then return 0'''
    elif int(S[0]) == 0:
        return 0 + baseBToNum(S[1:], B)
        '''have to int-ify string S so that it can be compared to integers. If the first number
        in the string is a 0 then a 0 is added. The fucntion is recursively called for the rest
        of the string'''
    elif int(S[0]) == 1:
        return B**(len(S) - 1) + baseBToNum(S[1:],B)
        '''if the first integer of the string is 1, then the base is raised to the length of the string minus 1. the minus
        1 is there because to account for the base raised to the 0 power. Then this number is added the recursive call of the function for
        rest of the numbers in the string'''

#print(baseBToNum('11' , 10))


def baseToBase (B1, B2, SinB1):
    '''that takes three inputs: a base B1, a base B2 (both of which are
    between 2 and 10, inclusive) and SinB1, which is a string representing a number in
    base B1. Returns a string representing the same number in base B2'''
    NumB2 =  numToBaseB(int(SinB1), B2)
    '''first have to convert the string SinB1 to an integer and covert the number in regards to the base B2.
    We can call this number NumB2.'''
    return baseBToNum(NumB2, B1)
    '''now that the NumB2 represents the string in terms of B2, we can return the conversion of NumB2 and
    the original base B1 to get the string representing the same number in base B2.'''

print(baseToBase(3, 2, '2'))

def add(S, T):
    '''takes two binary strings S and T as input and returns their sum, also in binary'''
    s = baseBToNum(S, 2)
    t = baseBToNum(T, 2)
    '''s and t are the conversions of the the 2 binary strings S, T into the to two base-10 numbers'''
    new_add = s + t
    '''new_add is the sum of the s and t'''
    return numToBaseB(new_add, 2)
    '''returns the sum of s and t into the base of 2'''

#print(add('100' , '111'))

# Each row has (x,y,carry-in) : (sum,carry-out)
FullAdder = \
{ ('0','0','0') : ('0','0'),
('0','0','1') : ('1','0'),
('0','1','0') : ('1','0'),
('0','1','1') : ('0','1'),
('1','0','0') : ('1','0'),
('1','0','1') : ('0','1'),
('1','1','0') : ('0','1'),
('1','1','1') : ('1','1') }

'''FullAdder library'''

def addBhelper(x, y, C):
    '''addB helper function. takes string x and y and uses C as the carry for the addition bits. Returns the addition of two strings binary without base conversion'''
    if x  == '' and y == '':
        if C == '0':
            return ''
        else:
            return C
        '''if the strings x and y are empty then if the carry is 0 then return an empty or return c its self'''
            
    elif x != '' and y != '':
        sumBit, carryBit = FullAdder[x[-1], y[-1], C]
        '''if x and y are not empty strings then set the sumBit and carryBit from the 
        FullAdder format equal to the string of the right most bit of the string x and y'''
        return addBhelper(x[:-1], y[:-1],carryBit) + sumBit
        '''recursion: recalls the function and applies what we did above to rest of the strings from the right bit to the left. 
        the carryBit stored and the sumBit is added to the end and keeps repeating'''
    
    elif x == '' and y != '':
        sumBit, carryBit = FullAdder['0', y[-1], C]
        '''if x is empty and y is not an empty string then set the sumBit and carryBit from the 
        FullAdder format equal --> x to 0 because x is empty, y compare to the rightmost bit, c is the carry'''
        return addBhelper(x, y[:-1],carryBit) + sumBit
        '''recursion: recalls the function and applies what we did above to rest of the strings from the right bit to the left, except for x because x is empty/0. 
        the carryBit is stored and the sumBit is added to the end and keeps repeating'''
    
    elif x!='' and y=='':
        sumBit, carryBit = FullAdder[x[-1],'0', C]
        '''if y is empty and x is not an empty string then set the sumBit and carryBit from the 
        FullAdder format equal --> y to 0 because y is empty, x compare to the rightmost bit, c is the carry'''
        return addBhelper(x[:-1],y,carryBit) + sumBit
        '''recursion: recalls the function and applies what we did above to rest of the strings from the right bit to the left, except for y because y is empty/0. 
        the carryBit is stored and the sumBit is added to the end and keeps repeating'''

def removeZero(x):
    '''removes the leading zeros from the sum of the strings'''
    if x[0] == '0' and len(x) != 1:
        return removeZero(x[1:])
        '''if the first term of the sum is a 0 and the length of the string is not 1 (so then if the sum is just 0 it will not output nothing)
        return the the rest of of the string and this is recursively done just in case there are more than 1 leading 0s'''
    else:
        return x
        '''if theres no leading zeros then return the orginal string'''
    
def addB(x, y):
    '''Takes two strings as input. These strings are the representations of binary numbers.
    Returns a new string representing the sum of the two input strings'''
    return removeZero(addBhelper(x,y,'0'))
    '''returns the helper with the remove leading zeros helper. the carry will always start as 0'''

