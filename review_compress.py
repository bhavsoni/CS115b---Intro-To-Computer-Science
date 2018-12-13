"""
CS 115 - TA Steph Oro
These are some function patterns -- ideas -- that
you may find useful for completing the compress
and uncompress functions.
"""



def periodic(c, x):
    """
    An arbitrary function meant to preform recursion while
    changing an argument c between 0, 1, 2, and 3. Something
    that requires an argument that can change between numbers
    in each successive recursive call will prove useful
    in compress and uncompress.

    The x argument is unnecessary, and solely exists to make
    this function recursive. You can use the idea of an
    argument that changes to build up compress and uncompress.
    """
    if(x == 0):
        return 0
    period = 4
    periodic((c + 1) % period, x - 1)

print("what's the importance of the a periodic function?")
print("how can we apply it to other functions?")


def transform1(s):
    """
    A more powerful model of string transformation
    than the simple one character at a time model you've
    dealt with thus far.

    Works by determining how much of the string to
    work with at a time, then modifying a chunk, and
    recursing over the rest of the string
    """
    def amount_consume(target, s):
        """
        Determine what chunk size you're dealing with -
        you'll certainly want to change this function.
        """
        if s == "":
            return 0
        target_len = len(target)
        if s[:target_len] == target:
            return 2 + amount_consume(target, s[target_len:])
        return 0
        
    def consume(chunk):
        """
        Do some work in transforming the chunk -
        you'll certainly want to change this function.
        """
        if(chunk == ""):
            return ""
        length = len(chunk)//2
        return chunk[0]*length + chunk[1]*length
    
    if s == "":
        return ""
    chunk_size = amount_consume(s[:2], s)
    chunk = s[:chunk_size]
    transformed_chunk = consume(chunk)
    return transformed_chunk + transform1(s[chunk_size:])

def transform2(s):
    """
    A more powerful model of string transformation
    than the simple one character at a time model you've
    dealt with thus far.

    Works by determining how much of the string to
    work with at a time, then modifying a chunk, and
    recursing over the rest of the string
    """
    def amount_consume(s):
        """ again amount_consume can be any function """
        return 5
    def consume(chunk):
        """ and consume can apply any process """
        return chunk[::-1]
    if s == "":
        return ""
    chunk_size = amount_consume(s)
    chunk = s[:chunk_size]
    transformed_chunk = consume(chunk)
    return transformed_chunk + transform2(s[chunk_size:])

print("what's the importance of the transform pattern?")
print("how can we apply it to other functions?")
print("transform1('ABABCDCDABABABUIJKJKJKJK') => " + transform1("ABABCDCDABABABUIJKJKJKJK"))
print("transform1('AB') => " + transform1("AB"))
print("transform1('ABab') => " + transform1("ABab"))
print("transform1('abab') => " + transform1("abab"))
print("transform1('1010101010101010') => " + transform1("1010101010101010"))
print()
print("transform2('ABCDEFGHIJKLMNOPQRSTUVWXYZ') => " + transform2("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
print("transform2('12345') => " + transform2("12345"))
print("transform2('123456') => " + transform2("123456"))
print("transform2('1234567') => " + transform2("1234567"))
print("transform2('0123456789') => " + transform2("0123456789"))



'''
def cycle(c, x):
    if x == 0:
        return c
    return cycle((c+1)%4, x-1)
    '''''' (0, 5)
        (1,4)
        (2,3)
        (3,2)
        (0,1)
        (1,0)...''''''

print (cycle(0,5))

def consume(s):
    return str(int(s) + 1)

def amountconsume (targ, s):
    if s == '': 
        return 0
    if s[:2] == targ:
        return 2 + amountconsume (targ, s[2:])
    return 0

def transform (s):
    if s == '':
        return s
    x = amountconsume(s[2:], s)
    c = consume(s[:x])
    return c + transform(s[x:])
    ''''''need to deal with blocks of string...given amount of blocks....need to transform the block of strings....
    given a certain amount you will need to return the transform of the string''''''

print (transform('aaaaahhhhhhmmmmmmmuiiiiiiiaaaaaa'))


'''


'''need to answer the things in coments'''


'''
64 1s 0s 1s 0s  --> need 5 1s = 31 0s 
in 64 1s there are 0 0s.    11111  00000

0s        1s        0s        1s     ...
11111    00000    11111      00000      00010
31 0s      0 0s    31 0s      0 0s      2 0s

00000    11111    00000    11111    00000    00010

'''