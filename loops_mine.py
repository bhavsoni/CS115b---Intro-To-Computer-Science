'''
Created on Mar 28, 2017

@author: BhavinSoni
'''
import random 

def map_sqr(lst):
    '''returns the the square of each of the elements in the list '''
    result = []
    for x in lst:
        result.append(x*x)
    return result
    

def map_sqr2(lst):
    return [x*x for x in lst] #lst comprehension


def average(lst):
    total = 0
    for x in lst:
        total += x 
    return total / len(lst)



# print(map_sqr([1,2,3,4]))
# print(map_sqr2([1,2,3,4]))
# print(average([1,2,3,4,5]))



def findMax(L):
    '''returns hte max value in the list L, if the list = [] returns none'''
    if L == []:
        return None
    maxValue = L[0]
    for x in L:
        if x > maxValue:
            maxValue = x
    return maxValue

def findMin(L):
    '''returns the min value in the list L, if the list = [] returns none'''
    if L == []:
        return None
    minValue = L[0]
    for x in L:
        if x < minValue:
            minValue = x
    return minValue

L = [1,3,5,2,4,6,-1,9]


def findMinMax(L):
    if L == []:
        return None
    minValue = maxValue = L[0]
    for x in L:
        if x > maxValue:
            maxValue = x
        elif x < minValue:
            minValue = x
    return (minValue, maxValue)
        
        
# print(findMax(L))
# print (findMin(L))
# print(findMinMax(L))

s = [3,4,5]
t=s
s[1]=2
'''s and t are aliases '''
# print(s)
# print(t)     

def shallow_copy(L):
#    new_list = []
#    for x in L:
#        new_list.append(x)
#        return new_list
    return [x for x in L]
        

'''
s = [1, [3,5], 12]
t = shallow_copy(s)
print(s)
print(t)
t[1][0] = 5
print(s)
print(t)'''


def deep_copy(L):
    new_list =[]
    for x in L:
        if type(x) is list:
            new_list.append(deep_copy(x))
        else:
            new_list.append(x)
    return new_list

# s = [1, [3,5], 12]
# t = deep_copy(s)
# print(s)
# print(t)
# t[1][0] = 5
# print(s)
# print(t)



def sum_matrix(matrix):
    total = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            total += matrix[row][col]
    return total

def sum_matrix2(matrix):
    total = 0
    for row in matrix:
        for x in row:
            total += x
    return total

def print_matrix(matrix):
    for row in range(len(matrix)):
        print (' ', end='')
        for col in range (len(matrix[row])):
            print (matrix[row][col], end=' ')
            print(' | ', end ='')   
        print()
    if row < 3: 
        print ('-' * 25)

def print_grid(grid):
    '''Formats a 3x3 matrix with ASCII art and prints it to the screen.'''
    for row in range(len(grid)):
        print(' ', end='')
        for col in range(len(grid[row])):
            print(grid[row][col], end=' ')
            if col < 2:
                print('|', end=' ')
        print()
        if row < 2:
            print('-' * 11)

# Make a 3x3 grid of random integers between 1 and 9.
grid = [[random.randint(1, 1) for _ in range(3)] for _ in range(3)]

matrix = [[random.randint(1, 1) for _ in range(4)] for _ in range(3)]
matrix1 =[[]]
print_matrix(matrix1)
            