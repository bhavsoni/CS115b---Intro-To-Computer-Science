'''
Created on _________2/12/17______________
@author:   _________BHAVIN SONI______________
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Hw 3
'''
# Be sure to submit hw3.py.  Remove the '_template' from the file name.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def giveChange(amount, coins):
    if amount == 0:
        return (0,[])
        '''if the amount is 0 it will return a 0 and empty set/tuple'''
    if coins == []:
        return (float('inf'), [])
        '''if the coins list is 0 then the it will retun the infinity and empty set'''
    elif (amount - coins[0]) < 0:
        return giveChange(amount , coins[1:])
        '''if the amount of the change given subtracted by the first coin in the list is less 0 
        return the loseit function and move to the next coin in the list'''
    useit = giveChange(amount-coins[0],coins)
    '''useit function recursively takes the amount and subtract it fromt he frist element in the coin to compare it 
    in order to determine whether to keep that value'''
    fxn = useit[0] + 1
    '''this helper function fxn is used to add 1 recursive to every useit function in order to count the min amount of coins/elemetns needed'''
    loseit = giveChange(amount,coins[1:])
    '''loseit basically keeps the amount value and goes through the other elements in the list'''
    if fxn < loseit[0]:
        return (fxn, [coins[0]] + useit[1])
        '''if the fxn is less than the first elemetn in loseit then it will add the fxn to the function and add it to the list
        because this would mean fxn has less moves and you want to return the least amount of moves and coins'''
    return loseit
    '''if the fxn is not less than loseit then the function will just return loseit because it produces the least amount of moves/elements'''

print (giveChange(40,[1,5,10,25,50]))


# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
' Hints: Use map. Feel free to use some of the functions you did for
' homework 2 (Scrabble Scoring). As always, include any helper
' functions in this file, so we can test it.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def letterScore(letter, scorelist):
    '''letter score: takes the letter in the scorelist and prints the value of that letter.'''
    if scorelist==[]:
        return 0
    '''if scorelist is empty then it prints an empty list. '''
    pair=scorelist[0]
    if letter == pair[0]:
        return pair[1]
    '''pair is the values of the pair of the letter and value then if the first list is equivalent to the letter, then the pair will return the letter value.'''
    return letterScore(letter,scorelist[1:])
    '''if not then the recursive is implemented to go throughout the list.'''

def wordScore(S,scorelist):
    '''the wordscore takes a string and the return the value of that word/string of letters.'''
    if S=='':
        return 0
    '''if the string s is empty then returns a value of 0.'''
    fxn=wordScore(S[1:],scorelist)
    '''the fxn(function) is defined as the recursive of the wordscore of the individual characters of the score list.'''
    let=letterScore(S[0],scorelist)
    '''then let is defined as the letterscore  of the individual characters of the scorelist'''
    return let+fxn
    '''these 2 functions are added to represent the value of the word.'''


def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.'''
    if dct == []:
        return []
        '''if the list of words in the dct is empty then return an empty list'''
    else:
        return [[dct[0], wordScore(dct[0], scores)]] + wordsWithScore(dct[1:], scores)
        '''returns the first word of the dct and the value of the first score. this part is in double brackets bc it 'listifies' 
        the word and its value and put it in a list of its own. This is then added to the recursive function which continuously
        returns the words in the dct list with its values and then adds it to a list. ''' 
   

print(wordsWithScore(Dictionary, scrabbleScores))
    
    
'''Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(scrabbleScores, Dictionary) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
'''


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n].'''
    if n == 0 or L == []:
        return []
    '''if the place you want to slice until is at the 0 index or the L is given is empty return an empty set'''
    return [L[0]] + take(n-1, L[1:])
    '''listify the first element of the list and add that to the recursive of the function take. 
    the recursive function takes the place you want to slice and subtracts 1 bc it is to the [0:n] not including n
    so it goes to the element before n and then prints the rest of the List to that n. '''




'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:].'''
    if n == 0 or L == []:
        return L
    '''if the place you want to slice until is at the 0 index or the L is given is empty return an empty set'''
    return drop(n-2, L[1:])
    '''like the take function. this time we dont need to add the first element of the list becasue we want to use
    the elements from the index n to the end of of the list. Therefore we take the n-1 in order to account for the 0 index
    and then L[1:] prints the rest of the list from that n to the of the of list'''



