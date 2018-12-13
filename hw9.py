'''
@author: Bhavin Soni
Pledge: I pledge my honor that I have abided by the Stevens Honor System

CS115 - Hw 9

Objective: To become familiar with imperative style and for and while loops_mine.

Instructions: Submit a copy of this file (with your name and pledge and) with
the incomplete functions completed. Don't change the functions that are
already implemented.

# Search for "TODO" to find the incomplete functions.
'''
from cs115 import map, reduce

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Exercise 1
' Study function questify(). Then implement questifyAlt() so that it gives
' the same results as questify(), using map and lambda but no helping function.
' Hint: adapt the body of addQuestmark().
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def questify(str_list):
    '''Assume str_list is a list of strings. Returns a list of
    the same strings but with ? suffixed to each.'''
    def addQuestmark(s):
        '''Adds a question mark to a string.'''
        return s + '?'

    return map(addQuestmark, str_list)

def questifyAlt(str_list):
    '''Same as questify'''
    return map(lambda x: x + '?' , str_list)
    '''maps the lambda of the string plus a question mark at the end of the string for every string in the
    str_list'''

#print(questifyAlt(['yeah', 'really', 'no way']))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Exercise 2
' Study functions leppard() and catenate(). Implement catenateLoop(), without
' using recursion or reduce or any built-in Python function. Instead, use a
' loop. In some ways your code will resemble the body of leppard().
' If you prefer, you can follow the style of leppardIndex(), but I suggest not.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def leppard(inputString):
    '''Mystery.'''
    outputString = ''
    for symbol in inputString:
        if symbol == 'o':
            outputString = outputString + 'ooo'
        else:
            outputString = outputString + symbol
    print(outputString)

def leppardIndex(inputString):
    '''Same as leppard(), but using an integer index rather than directly
    referring to elements of the input string.'''
    outputString = ''
    for i in range(len(inputString)):
        if inputString[i] == 'o':
            outputString = outputString + 'ooo'
        else:
            outputString = outputString + inputString[i]
    print(outputString)

def catenate(str_list):
    '''Assume str_list is a list of strings.
    Return a single string, their catenation.'''
    if str_list == []:
        return ''
    return reduce(lambda s, t: s + t, str_list)

def catenateLoop(str_list):
    '''Same as catenate'''
    string = ''
    '''originally set value of string to '' '''
    for x in str_list:
        string = string + x
        '''x is used as a way to keep adding strigns together for however many strings in the list. 
        the string now equals the original string plus one string from the list for however strings there are'''
    return string
    '''function returns the final catenate of the strings'''

#print (catenateLoop(['this', 'function', 'actually', 'works']))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Exercise 3
' Implement letterScoreLoop using --you guessed it-- a loop instead of
' recursion. Also, do not use map or reduce.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
scrabbleScores = [["a", 1], ["b", 3], ["c", 3], ["d", 2], ["e", 1], ["f", 4], \
                  ["g", 2], ["h", 4], ["i", 1], ["j", 8], ["k", 5], ["l", 1], \
                  ["m", 3], ["n", 1], ["o", 1], ["p", 3], ["q", 10], ["r", 1], \
                  ["s", 1], ["t", 1], ["u", 1], ["v", 4], ["w", 4], ["x", 8], \
                  ["y", 4], ["z", 10]]

aDictionary = ["a", "am", "at", "apple", "bat", "bar", "babble", "can", "foo", \
               "spam", "spammy", "zzyzva"]

def letterScore(letter, scorelist):
    '''Assume scorelist is a list of lists [ltr, val] where ltr is a single
    letter and val is a natural number. Assume letter is a single letter string,
    that occurs in scorelist. Return the associated value.'''
    if letter == scorelist[0][0]:
        return scorelist[0][1]
    return letterScore(letter, scorelist[1:])

def letterScoreLoop(letter, scorelist):
    '''Same as letterScore'''
    # HINTS: You can rely on the assumption that letter occurs in scorelist.
    # It may be helpful to use an if-statement without an else.
    x = range(len(scorelist) - 1)
    '''x = the range of the length of the scorelist -1. this is bc we want the for loop to run this many times
    in order to account for the letter and value in the scrabbleScores'''
    for x in scorelist:
        if x[0] == letter:
            return x[1]
            '''for the x in the scorelist (scrabbleScores), the function loops_mine such that if the first element
            of x is equivalent to the letter desired, then it will return the second element of x which is the letterscore'''
    
        

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Exercise 4
' Implement wordScoreLoop using a loop instead of recursion. (And don't
' use map or reduce.)
' Use letterScore() or letterScoreLoop(); it shouldn't matter which one.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def wordScore(S, scorelist):
    '''Assume S is a string and scorelist is in the format above and
    includes every letter in S. Return the scrabble score of that string.'''
    if S == '':
        return 0
    return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)

def wordScoreLoop(S, scorelist):
    '''Same as wordScore'''
    x = range(len(S)-1)
    '''x represents the range of the length of the string -1, this is used represent the letters in S''' 
    y = 0
    '''y is value of the word and is set to 0 as a base case'''
    for x in S:
        y = y + letterScore(x, scorelist)
        '''y equals the original y + the letterscore for the range of x (which will go through every letter in S) and apply that to
        the scorelist (scrabbleScores). this will loop and will keep adding the letter scores from S to y creating a new value fo y all the time
        until there are no more letters in S'''
    return y
    '''returns the value of the word'''


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Exercise 5
' Implement wordsWithScoreLambda using a lambda instead of the helper scoreWord.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def wordsWithScore(dct, scores):
    '''Assume dct is a list of words and scores is a list of [letter, number]
    pairs. Return a copy of the dictionary, annotated so each word is paired
    with its value. For example, wordsWithScore(scrabbleScores, aDictionary)
    should return [["a", 1], ["am", 4], ["at", 2] ...etc... ]'''
    def scoreWord(wrd):
        return [ wrd, wordScore(wrd, scores) ]

    return map(scoreWord, dct)

def wordsWithScoreLambda(dct, scores):
    '''Same as wordsWithScore'''
    return map(lambda wrd: [wrd, wordScore(wrd, scores )], dct)
    '''same thing as above but without helper. map the lambda of wrd, which maps the word score with
    dct resulting in the words with the scores in the list '''


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Exercise 6
' Implement wordsWithScoreLoop using a loop instead of map or recursion.
' Be careful NOT to change the dictionary.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def wordsWithScoreLoop(dct, scores):
    '''Same as wordsWithScore'''
    x = range(len(dct) -1)
    '''x is the the range of the length of the dictionary -1, this acts like a splice for the loop'''
    y = []
    '''y is the reuslt and so it is initially set to an empty list'''
    for x in dct:
        y  = y + [[x, wordScore(x, scores)]]
        '''for the the range of x in the dct, the result, y, equals the original y plus the 
        list of the range values of the x with the wordscore of the x and scores. This keeps loops_mine for therange of x
        and adds new words with scores to the y list.'''
    return y
    '''retuns the final list with the lists of the words and vlaues'''
