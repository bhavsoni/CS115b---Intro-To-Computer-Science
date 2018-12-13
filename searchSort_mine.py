'''
Created on Apr 10, 2017

@author: BhavinSoni
'''
import random
import time

def sequential_search(lst,key):
    '''searches list ofr key and returns the index of the key in that list otherwise it returns -1'''
    for x in range(len(lst)):
        if lst[x] == key:
            return x
    return -1

#lst = [5,9,-2,-12,7]

#print(sequential_search(lst,-34))

def binary_search(lst, key):
    '''searches list for key and returns the index of the key in that list otherwise it returns -low -1
    ONLY WORKS IF LIST IS SORTED '''
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

#lst = [1,3,5,7,9,10,11]
#print(binary_search(lst, 1))
#key = -1
#index  = binary_search(lst, key)
#if index >= 0:
#    print('key %d found at index %d' % (key, index))
#else:
#    print ('key %d not found but can be inserted at index %d' % (key, -index - 1))
    

#lst  = [random.randint(1,100000) for _ in range(500000)]
#lst.sort()
#start = time.clock()
#sequential_search(lst, 200000)
#elapsed = (time.clock() - start) * 1000


#start = time.clock()
#binary_search(lst, 200000)
#elapsed = (time.clock() - start) * 1000

'''bigO of sequenstial sort = n
big O of binary sort = log base 2 n'''




def swap (lst, i, j):
    '''lst, i and j are indecies'''
    temporary = lst[i]
    lst[i] = lst[j]
    lst[j] = temporary
    
'''selection sort always makes n(n-1)/2 comparisons
therefore selection sort is O(n^2) => big O of n^2 (since bigger n means its slower and takes more time)

selection sort takes n-1 swaps.
'''
    
def selection_sort(lst):
    n = len(lst)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        if i != min_index:
            swap(lst, i, min_index)
    return lst

ab = [random.randint(1,9) for _ in range (0)]
print(selection_sort(ab))

'''selection_sort(lst)
start = time.clock()
lst.sort()
elapsed = (time.clock() - start) * 1000
print('time elapsed : %d' % elapsed)

lst = [random.randint(1,10000) for _ in range (10000)]
selection_sort(lst)
start = time.clock()
selection_sort(lst)
elapsed = (time.clock() - start) * 1000
print('time elapsed : %d' % elapsed)'''