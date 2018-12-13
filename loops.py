'''
Created on Mar 28, 2017
Last modified on Apr 5, 2017

@author: Brian Borowski
Examples of loops, aliases, shallow copy, deep copy, and 2-dimensional lists.
'''
# import random
# 
# def map_sqr(lst):
#     '''Will return exactly the same thing as map(sqr, lst). In other words,
#     returns a new list with each element in the original list squared.'''
#     result = []
#     for x in lst:
#         result.append(x * x)
#     return result
# 
# def map_sqr2(lst):
#     '''Will return exactly the same thing as map(sqr, lst). In other words,
#     returns a new list with each element in the original list squared.'''
#     return [x * x for x in lst] # list comprehension
# 
# def average(lst):
#     '''Computes the average of the numbers in a list by first finding the sum
#     of the values and then dividing by the number of values in the list.'''
#     total = 0
#     for x in lst:
#         total += x
#     return total / len(lst)
# 
# print(map_sqr([1, 2, 3]))
# print(map_sqr2([1, 2, 3]))
# print(average([1, 2, 3]))

def find_max(L):
    '''Returns the maximum value in the list L. If the list is empty, the
    function returns None.'''
    if L == []:
        return None
    max_val = L[0]
    for x in L:
        if x > max_val:
            max_val = x
    return max_val

def find_max2(lst):
    '''Returns the maximum value in the list L. If the list is empty, the
    function returns None.'''
    if lst == []:
        return -1
    max_index = 0
    for i in range(len(lst)):
        if lst[i] > lst[0]:
            max_index = i
    return max_index

lst = [1,2,3,4,5]
L = [1,23,45,2,16,13]

print(find_max(L))
print(find_max2(lst))
# def find_min(L):
#     '''Returns the minimum value in the list L. If the list is empty, the
#     function returns None.'''
#     if L == []:
#         return None
#     min_val = L[0]
#     for x in L:
#         if x < min_val:
#             min_val = x
#     return min_val
# 
# def find_min_max(L):
#     '''Returns a tuple of the minimum and maximum values in the list L.
#     If the list is empty, the function returns None.'''
#     if L == []:
#         return None
#     max_val = min_val = L[0]
#     for x in L:
#         if x > max_val:
#             max_val = x
#         elif x < min_val:
#             min_val = x
#     return (min_val, max_val)
# 
# print(find_max([1, 3, 5, 2, 4, 6, -9]))
# print(find_min([1, 3, 5, 2, 4, 6, -9]))
# print(find_min_max([1, 3, 5, 2, 4, 6, -9]))
# 
# def shallow_copy(L):
#     '''Makes a shallow copy (1 level deep) of the elements in L and stores them
#     in a new list.'''
#     return [x for x in L]
# 
# def deep_copy(L):
#     '''Makes a deep copy of a list, that is, copies all elements including
#     lists within lists.'''
#     new_list = []
#     for x in L:
#         if type(x) is list:
#             new_list.append(deep_copy(x))
#         else:
#             new_list.append(x)
#     return new_list
# 
# # Aliases
# S = [3, [1, 2], 9]
# T = S  # T is an alias for S
# print(T is S) # True, since S and T point to the same list.
# # The ids are equal.
# print(id(S))
# print(id(T))
# 
# # Shallow copy
# S = [3, [1, 2], 9]
# T = shallow_copy(S)
# print(T is S) # False, since S and T do not point to the same list.
# print(S)
# print(T)
# # Notice how modifying the value in a nested list changes both S and T.
# T[1][0] = 0
# print(S)
# print(T)
# 
# # Deep copy
# S = [3, [1, 2], 9]
# T = deep_copy(S)
# print(S)
# print(T)
# # Notice how modifying the value in a nested list changes only T, the
# # list which was modified.
# T[1][0] = 0
# print(S)
# print(T)
# 
# def sum_matrix(matrix):
#     '''Returns the sum of all the values in a 2-dimensional list.
#     Uses row and col indexes.'''
#     total = 0
#     for row in range(len(matrix)):
#         for col in range(len(matrix[row])):
#             total += matrix[row][col]
#     return total
# 
# def sum_matrix2(matrix):
#     '''Returns the sum of all the values in a 2-dimensional list.
#     Uses the foreach loops.'''
#     total = 0
#     for row in matrix:
#         for x in row:
#             total += x
#     return total
# 
# def print_grid(grid):
#     '''Formats a 3x3 matrix with ASCII art and prints it to the screen.'''
#     for row in range(len(grid)):
#         print(' ', end='')
#         for col in range(len(grid[row])):
#             print(grid[row][col], end=' ')
#             if col < 2:
#                 print('|', end=' ')
#         print()
#         if row < 2:
#             print('-' * 11)
# 
# # Make a 3x3 grid of random integers between 1 and 9.
# grid = [[random.randint(1, 9) for _ in range(3)] for _ in range(3)]
# 
# print(grid)
# print(sum_matrix(grid))
# print(sum_matrix2(grid))
# print_grid(grid)
