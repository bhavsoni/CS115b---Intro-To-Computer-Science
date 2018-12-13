'''
Created on Feb 8, 2017

@author: BhavinSoni

'''



def change(amount, coins):
    if amount == 0:
        return 0
    if coins == []:
        return float('inf')
    loseit= change(amount, coins[1:])
    if coins[0]> amount:
        return loseit
    useit=change(amount-coins[0],coins)+1
    return min(loseit,useit)

print (change(40,[1,5,10,25,50]))

def fastchange(amount, coins):
    def changehelper (amount, coins, memo):
        if (amount, coins) in memo:
            return memo[(amount, coins)]
        
        if amount == 0:
            result = 0
        elif coins == []:
            result = float('inf')
        else:
            loseit = changehelper(amount, coins[1:], memo)
            if coins[0]> amount:
                return loseit
            useit = changehelper(amount-coins[0],coins, memo)+1
            return min(loseit,useit, memo)
    
        memo[(amount, coins)] = result
        return result
    
    return changehelper(amount, tuple(coins), {})

print (fastchange(40,[1,5,10,25,50]))

def giveChange(amount, coins):
    if amount == 0:
        return (0,[])
    if coins == []:
        return (float('inf'), [])
    elif (amount - coins[0]) < 0:
        return giveChange(amount , coins[1:])
    useit = giveChange(amount-coins[0],coins)
    fxn = useit[0] + 1
    loseit = giveChange(amount,coins[1:])
    if fxn < loseit[0]:
        return (fxn, [coins[0]] + useit[1])
    return loseit


