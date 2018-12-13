'''
Created on Apr 13, 2015
Last modified on April 7, 2016

@author: Brian Borowski

CS115 - Functions that merge lists
'''
def num_matches(list1, list2):
    '''Returns the number of elements that the two lists have in common.'''
    list1.sort()
    list2.sort()
    matches = 0
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            matches += 1
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return matches

def merge(list1, list2):
    '''Returns the elements of the two lists merged into one, eliminating
    duplicates.'''
    list1.sort()
    list2.sort()
    result = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            result.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    while i < len(list1):
        result.append(list1[i])
        i += 1
    while j < len(list2):
        result.append(list2[j])
        j += 1
    return result

def keep_matches(list1, list2):
    '''Returns a list of the elements that the two lists have in common.'''
    list1.sort()
    list2.sort()
    result = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            result.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return result

def drop_matches(list1, list2):
    '''Returns a list that contains no matches between elements of list1 and
    list2.'''
    list1.sort()
    list2.sort()
    result = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    while i < len(list1):
        result.append(list1[i])
        i += 1
    while j < len(list2):
        result.append(list2[j])
        j += 1
    return result

if __name__ == '__main__':
    A = [2, 3, 5, 7, 9, 11, 13, 17, 23]
    B = [11, 13, 15, 17, 19, 21, 23, 25, 27]
    print('List A:        %s' % A)
    print('List B:        %s' % B)
    print('Merged lists:  %s' % merge(A, B))
    print('Total matches: %d' % num_matches(A, B))
    print('Matches:       %s' % keep_matches(A, B))
    print('Unique:        %s' % drop_matches(A, B))
