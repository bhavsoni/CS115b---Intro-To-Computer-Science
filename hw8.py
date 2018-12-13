'''
Created on Mar 27, 2017

@author: BhavinSoni
pledge: I pledge my honor that I have abided by the Stevens Honor System
'''

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
    
def flipBit(s):
    '''helper function that flips each of the bits in the string: 1--> 0 and 0-->1'''
    if s == '':
        return s
    '''if empty string return empty string'''
    if s[0] == '1':
        return '0' + flipBit(s[1:])
        '''if the first it is 1 then switch it to 0 and do that for the rest of the string'''
    if s[0] == '0':
        return '1' + flipBit(s[1:])
        '''if the first it is 0 then switch it to 1 and do that for the rest of the string'''

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
    
def addB(x, y):
    '''Takes two strings as input. These strings are the representations of binary numbers.
    Returns a new string representing the sum of the two input strings'''
    return addBhelper(x,y,'0')
    '''returns the addition of the two strings, with the carry set as 0'''
 
     
def TcToNum(s):
    '''takes as input a string of 8 bits representing an integer in two's-complement, 
    and returns the corresponding integer'''
    if s[0] == '0':
        return binaryToNum(s)
        '''if the first bit of the string is a 0 then return the integer of the binary string'''
    elif s[0] == '1':      
        return -1 * binaryToNum(flipBit(addB('11111111',s)))
        '''if the fist bit of the string is one then the function will return the addition 
        of -1 (11111111) (this is because in order to convert to two complement have to subtract 1)
        and the string input, then the code would be flipped (switchings the 1 and 0s) then converted to binary
        integer. This is then multiplied by -1 to get the complement of the string'''


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
    
def paddingfunc(N):
    '''this is a helper functions that pads 0s to the function to make it a 8 bit string'''
    if len(N) < 8:
        N = "0" + N
        return paddingfunc(N)
        '''if the length of the string is less than 8, then the new string N will keep adding 0s until length of 8'''
    else:
        return N
        '''if length of string is already 8 then return the string'''


def NumToTc (N):
    ''' takes as input an integer N, and returns a string representing the two's-complement representation of that integer. '''
    if N < 128 and N >= 0:
        return paddingfunc(numToBinary(N))
        '''if in N is 0 or greater or less than 128, then print the padding of the conversion of the N to binary'''
    elif N >= -128 and N < 0:
        return addB(flipBit(paddingfunc(numToBinary((-1 * N)))),"1")
        '''if the integer is greater than or equal to -128 and less than 0, then
        convert the negative N to binary then pad that function to convert it to a 8bit length string 
        then flip the bits in order to convert into the two complements and then add the base of that to the string of 1 to return the 
        complement of the number'''
    else:
        return 'Error'
        '''if integer is out of range then it will print out Error'''



        