'''
Created on __2/25/17_____________________
@author:   __BHAVIN SONI_____________________
Pledge:    ____I pledge my honor that I have abided by the Sevens Honor System___________________

CS115 - Hw 5
'''
import turtle  # Needed for graphics

#draw tree in recursive function..... call recursive from inside 
# another function and then do turtle.done

# Ignore 'Undefined variable from import' errors in Eclipse.


def sv_treeHelper(trunk_length, levels):
    if levels == 0:
        return 
        '''once the levels reaches 0 it will stop...return nothing'''
    else:
        turtle.forward(trunk_length)
        '''turtle will move forward the initial length'''
        turtle.left(45)
        '''turtle will face 45 degrees to the left'''
        sv_treeHelper(trunk_length / 2, levels - 1)
        '''recursive call for the first branch... will go forward half the distance for the first length and that will be first level so it will subtract 1 each time until it reaches 0'''
        turtle.right(90)
        '''turtle turns 90 degrees to the right'''
        sv_treeHelper(trunk_length / 2, levels - 1)
        '''recursive call again for the second branch...see previous docstring for explanation'''
        turtle.left(45)
        '''returns the turtle to the initial 45 degrees position''' 
        turtle.backward(trunk_length)
        '''returns to the initial trunk of the tree'''
        
def sv_tree(trunk_length, levels):
    turtle.left(90)
    '''faces upward'''
    sv_treeHelper(trunk_length,levels)
    turtle.done

'''
def lucas(n):
    if n <= 0:
        return 2
    elif n == 1:
        return n
    return lucas(n-1) + lucas(n-2)

this function is just for my own reference
'''

def fast_lucas(n):
    '''Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]'''
    def fastLucasHelper(n, memo):
        if n in memo:
            return memo[n]
        if n <= 0:
            result = 2
        elif n == 1:
            result = n
        else:
            result = fastLucasHelper(n-1, memo) + fastLucasHelper(n-2, memo)
        
        memo[n] = result
        return result
    
    return fastLucasHelper(n,{})


def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    def fast_change_helper(amount, coins, memo):
        '''helper function for the memoization'''
        if (amount, coins) in memo:
            return memo[(amount,coins)]
            '''checks if the parameters are in the memo...
            if key is in dictionary, return value associated with key'''
        
        elif amount == 0:
            result = 0
            '''if the amount given is 0 the the cahnge will also be 0'''
        
        elif coins == ():
            result = float('inf')
            '''if the coins is empty...the function return infinity'''
            
        elif amount < coins[0]:
            return fast_change_helper(amount, coins[1:], memo)
            '''if the amount given is less thn the first coin in the list,
            it will return the next coin in the list until the amount>coin''' 
            
        else:
            useit = fast_change_helper(amount-coins[0],coins, memo) + 1
            '''the coins is used for the change and the substracted from the amount.
            every coin used a +1 is added as a counter'''
            loseit = fast_change_helper(amount, coins[1:], memo)
            '''lose it the same thing as define above after amount < coins[0]'''
            result = min(useit, loseit)
            '''return the minimum of change of the coins used'''
            
        memo[(amount, coins)] = result
        return result
        '''implement the memo and  stores the result in the dictionary and returns the result'''
    # Call the helper. Note we converted the list to a tuple.
    return fast_change_helper(amount, tuple(coins), {})

# If you did this correctly, the results should be nearly instantaneous.
print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))

# Should take a few seconds to draw a tree.
sv_tree(100, 4)
