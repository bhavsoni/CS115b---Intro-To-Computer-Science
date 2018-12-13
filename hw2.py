'''
Created on ___________02/04/17____________
@author:   __________BHAVIN SONI_____________
partner: Aaron John
Pledge:    I pledge my honor that I have abided by the Stevens Honor System
                    --Bhavin Soni
CS115 - Hw 2
'''
import sys
from cs115 import map, filter


# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.

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



def scoreList(Rack):
    '''score list takes the list of strings and prints out the possible words from that list'''
    def count (letter, lst):
        '''helper function that counts the amount of letters in the word(lst). '''
        if lst == '' or lst==[]:
            return 0
        if letter==lst[0]:
            return count(letter, lst[1:])+1
            '''using the recursive the function returns the count plus 1 if the first letter is equal to the first element in the lst.'''
        return count(letter,lst[1:])
        '''if not it returns the recursive of the rest of the elements in the lst.'''
    
    def canSpell(rack, word):
        '''helper function to see if we can spell the word, so we need a rack of  letters but just need to find a word within that rack.'''
        if word=='':
            return True
        if count(word[0], word) > count(word[0],rack):
            return False
            '''if the count of the characters in the word is greater than that of the count letters in the rack then the return is false.'''
        return canSpell(rack, word[1:])
        '''if not then use the recursive to find the spelling of the word in the rack'''
    lst=filter(lambda word: canSpell(Rack,word), Dictionary)
    '''lst = use the filter function to to check if the rack of letters can form a word so that it correlates to the dictionary'''
    return map(lambda word:[word,wordScore(word,scrabbleScores)],lst)
    '''map goes through the words in the dictionary and makes a new list and fills it in with the word and the score of the word for all of the Rack input.  the lst will help correlate the words and letters to the dictionary '''



def bestWord(Rack):
    '''best word returns the best value word out of the string.'''
    options=scoreList(Rack)
    '''options is used to compare the possible choices of the vlaue of words within a given rack of strings'''
    def best_option(option):
        '''compares the best_option to the cur (current) option (word)
then it continuously switches the current option as the range of the list of options 
and then checks if the first word/string is grater than the current one, and if it does
then it returns the first string. If not then it returns the current.'''
        if option==[]:
            return ['',0]
        first=option[0]
        '''first string from the options function'''
        cur=best_option(option[1:])
        '''goes through the option and takes in the next string in the list as a way to comapre the first string to that of the new one (current)'''
        if first[1]>cur[1]:
            return first
        else:
            return cur
    return best_option(options)
    ''' The function is then checked recursively to find the best word.'''
