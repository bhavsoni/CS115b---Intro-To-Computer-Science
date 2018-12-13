'''
Created on Mar 28, 2017

@author: BhavinSoni
'''

import random

MAX_TRIES = 7

print('''---welcome to  guess my number --- 

im thinking of a number between 1 and 100.
try to guess the number in %d ''' % MAX_TRIES, end = '') #the 'end' keeps the cursor on the same line 

if MAX_TRIES == 1:
    print(' atempt...')
else:
    print(' atempts...')
    
#set the inital values 
number = random.randint(1,100)  # generates a random number in [1,100]
tries = 1
guess = int(input('enter guess %d: ' %tries))

#guessing loop
while guess != number:
    if guess > number:
        print ('    input lower number ...')
    else:
        print ('    input higher number...')
        
    tries += 1
    if tries > MAX_TRIES:
        break 
    guess = int(input('enter guess %d: ' %tries))

'''break exits the loop and transferring execution to the line of code immediately after the loop'''
'''continue = transfers execution back to the start of the loop 
(loop condition) skipping lines of code)'''
    
if tries <= MAX_TRIES:
    print ('congrats mofo you guess the number %d in %d ' % (number, MAX_TRIES), end='')
else:
    print('sorry mofo you did not guess the number %d in %d ' % (number, MAX_TRIES), end='')

if  MAX_TRIES == 1:
    print (' try ')

else:
    print (' tries ')