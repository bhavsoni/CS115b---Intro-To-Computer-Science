'''
Created on _______3/8/17________________
@author:   ______Bhavin Soni_________________
partner: Aaron John
Pledge:    ______I pledge my honor that I have abided by the Stevens Honor System _________________

CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
from builtins import str
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

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
'''The functions above are imported from Lab 6'''
   
def counter(x, y):
    '''basically a counter for the number 1s and 0s in a string...uses y as a  placeholder for the amount of 1s or 0s'''
    if x == '':
        return 0
    elif x[0] == y:
        return 1 + counter(x[1:], y)
    else:
        return 0


def pad_zeros(x):
    '''basically adds/pads 0s to the string of bits less than the 5 bit chunk of strings needed'''
    return (COMPRESSED_BLOCK_SIZE - len(x)) * "0" + x


def compress(s):
    ''' function that takes a binary string S of length 64 as input and returns another binary string as output'''
    switch = {'0':'1','1':'0'}
    '''the switch state here helps switch the function to account for 0 and 1 to 1 and 0, covers the base for either to be next to each other in a sequence'''
    def helper(x, y):
        if x == '':
            return ''
        a = min(counter(x, y), MAX_RUN_LENGTH)
        ''' a is the minimum number used for the 1s and 0s and for the max run length in order to compress the bit of strings'''
        return pad_zeros(numToBinary(a)) + helper(x[a:], switch[y])
        '''function returns the pad of bit strings and covert it to binary and recursively repeats for all the bits'''
        
    return helper(s, "0") 


"""The largest number of bits that the compress algorithm could possibly use to encode a 64-bit 
    string/image is '10'* 32 = '00000' + '0000100001' * 32 = 325 bits because it uses every bit it has to produce an entire chunk of 5 bits
    in the compressed image, and above that, adds the 00000 padding."""




def uncompress(C):
    '''basically takes the string of the output given within the compress function above and returns. it is the opposite of what compress does'''
    if C == '':
        return ''
    segment = binaryToNum(C[:5]) * "0" + binaryToNum(C[5: 10]) * '1' 
    return segment + uncompress(C[10:])
    '''segment is basically takes the binary to number function and applies it to the first 5 terms by mutiplying by 0s and the second half of it is 1s
    the rest is then added and repeated using recursion'''
    


def compression (S):
    '''return the ratio of the compressed size to the original size for image S.'''
    return len(compress(S)) /len(S)


"""Using the compression test and the penguin and smile and five tests provided it was shown the penguin ratio was larger than that of the smile and five.
because there were more 0s and 1s than that of the smile and five. This also mean the compressed bit sizes were larger for the penguin as opposed to
the other tests.
Penguin = 1.484375
Smile = 1.328125 
Five = 1.015625 """




'''Professor Lai is essentially 'lai-ing' (lying) because its not possible/or takes a tremendous amount of skill
to make a code that will produce the shorten binary possible. This could only work for longer codes that have longer bits
to compress because the bits are the same and thus making the string shorter than its original. He wont be able to make
shorter strings shorter because in the end shorter codes will mean that the compressed bits are shorter making the output longer
than the original.  '''

print (compress("0"*9 + "01100110"*3 + "0"*9 + "00001000" + "01000010" + "01111110" + "0"*9))
print (compression("0"*9 + "01100110"*3 + "0"*9 + "00001000" + "01000010" + "01111110" + "0"*9))