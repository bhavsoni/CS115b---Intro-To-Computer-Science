'''
Created on _____2/24/17__________________
@author:   _____BHAVIN SONI__________________
Pledge:    _____I have pledge my honor that I have abided by the Stevens Honor System
                            --Bhavin Soni__________________

CS115 - Lab 5
'''
import time
from cs115 import map

words = []
HITS = 10

def fastED(first, second):
    '''Returns the edit distance between the strings first and second. Uses
    memoization to speed up the process.'''
    def fastEDhelper(first, second, memo):
        if (first, second) in memo:
            return memo [(first, second)]
        if first == '':
            result = len(second)
        elif second == '':
            result = len(first)
        elif first[0] == second[0]:
            result = fastEDhelper(first[1:], second[1:], memo)
        else:
            substitution = 1 + fastEDhelper(first[1:], second[1:],memo)
            deletion = 1 + fastEDhelper(first[1:], second, memo)
            insertion = 1 + fastEDhelper(first, second[1:],memo)
            result = min(substitution, deletion, insertion)
        
        memo[(first,second)] = result
        return result
    
    return fastEDhelper(first, second, {})

#print(fastED("antidisestablishment", "antiquities"))

def getSuggestions(user_input):
    '''For each word in the global words list, determine the edit distance of
    the user_input and the word. Return a list of tuples containing the
    (edit distance, word).
    Hint: Use map and lambda, and it's only one line of code!'''
    return map(lambda z: (fastED(z,user_input),z),words)

def spam():
    '''Main loop for the program that prompts the user for words to check.
    If the spelling is correct, it tells the user so. Otherwise, it provides up
    to HITS suggestions.

    To exit the loop, just hit Enter at the prompt.'''
    while True:
        user_input = input('spell check> ').strip()
        if user_input == '':
            break
        if user_input in words:
            print('Correct')
        else:
            start_time = time.time()
            suggestions = getSuggestions(user_input)
            suggestions.sort()
            endTime = time.time()
            print('Suggested alternatives:')
            for suggestion in suggestions[:HITS]:
                print(' %s' % suggestion[1])
            print('Computation time:', endTime - start_time, 'seconds')
    print('Bye')

if __name__ == '__main__':
    f = open('3esl.txt')
    for word in f:
        words.append(word.strip())
    f.close()
    spam()
