'''
Created on Apr 6, 2017

@author: BhavinSoni
'''
list1 = ['a', 'c' , 'd', 'f']
list2 = ['e', 'c' , 'b', 'a']

def num_matches(list1, list2):
    '''retuns the number of elements that are both in list 1 and list 2'''
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




def keep_matches(list1, list2):
    '''retuns the list of elements that are both in list 1 and list 2'''
    list1.sort()
    list2.sort()
    matches = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            matches.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return matches


def drop_matches(list1, list2):
    '''retuns the list of elements that are NOT in both list 1 and list 2'''
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


print (num_matches(list1, list2))
print (keep_matches(list1, list2))
print (drop_matches(list1, list2))