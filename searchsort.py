'''
Created on Apr 10, 2017

@author: Brian Borowski
CS 115 - Sequential search, binary search, selection sort
'''
import random
import time

def swap(lst, i, j):
    '''Swaps lst[i] with lst[j].'''
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp
    
def selection_sort(lst):
    '''Sorts the list in non-decreasing order (ascending with possible
    duplicate values.'''
    n = len(lst)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        if i != min_index:
            swap(lst, i, min_index)

def sequential_search(lst, key):
    '''Searches the list for the key. If the key is present, the function
    returns the index of the key. Otherwise, it returns -1.'''
    for i in range(len(lst)):
        if lst[i] == key:
            return i
    return -1

def binary_search(lst, key):
    '''Searches the list for the key. If the key is present, the function
    returns the index of the key. Otherwise, it returns -low - 1.
    NOTE: binary search works only if the list is sorted.'''
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if lst[mid] == key:
            return mid
        if lst[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -low - 1

lst = [5, 9, -2, -12, 7]
key = -121
index = sequential_search(lst, key)
if index >= 0:
    print('Key %d found at index %d.' % (key, index))
else:
    print('Key %d not found.' % key)

lst = [1, 3, 5, 7, 9, 10, 11]
key = 3
index = binary_search(lst, key)
if index >= 0:
    print('Key %d found at index %d.' % (key, index))
else:
    print('Key %d not found, but can be inserted at index %d.' % (key, -index - 1))
    
lst = [random.randint(1, 100000) for _ in range(20000)]
lst.sort()

start = time.clock()
sequential_search(lst, 200000)
elapsed = (time.clock() - start) * 1000
print('Sequential search: %0.3f ms' % elapsed)

start = time.clock()
binary_search(lst, 200000)
elapsed = (time.clock() - start) * 1000
print('Binary search:     %0.3f ms' % elapsed)

lst = [random.randint(1, 100000) for _ in range(10000)]
start = time.clock()
selection_sort(lst)
elapsed = (time.clock() - start) * 1000
print('Selection sort:    %0.3f ms' % elapsed)

lst = [random.randint(1, 100000) for _ in range(10000)]
start = time.clock()
lst.sort()
elapsed = (time.clock() - start) * 1000
print('Python sort:       %0.3f ms' % elapsed)
