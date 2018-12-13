'''
Created on Feb 17, 2017

@author: BhavinSoni
'''

def knapsack(capacity, itemList):
    if itemList == [] or capacity == 0:
        return [0,[]]
    
    if itemList[0][0] > capacity:
        return knapsack(capacity, itemList[1:])
    
    else:
        helperfxn = knapsack(capacity - itemList[0][0], itemList[1:])
        useit = [helperfxn[0] + itemList[0][1], [itemList[0]] + helperfxn[1]]
        loseit = knapsack(capacity, itemList[1:])
        if useit [0] > loseit[0]:
            return useit
        return loseit

print(knapsack(76, [[36, 35], [10, 28], [39, 47], [8, 1] , [7, 24] ]))