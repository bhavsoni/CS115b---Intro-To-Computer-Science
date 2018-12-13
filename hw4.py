'''
Created on Feb 20, 2017

@author: BhavinSoni
pledge: I pledge my honor that I have abided by the Stevens Honor System  
                                        -- Bhavin Soni

'''

def pascal_row (n):
    '''takes integer n and outputs a list of elements found in
    of that specific row of the Pascal triangle '''
    if n == 0:
        return [1]
    '''pascal triangel starts with row 0 which is just 1 : 
    this is the base case'''
    def adjacentTerm(r):
        '''helper function that takes into account the adjacent
        terms in each row and adds them together'''
        if len(r) == 1:
            return []
            '''want to return an empty list if the length of the 
            list is 1 bc you cant add a single term'''
        return [r[0] + r[1]] + adjacentTerm(r[1:])
        '''adds the first term and the second term of the list and
        recursively does that for each adjacent term'''
    return [1] + adjacentTerm(pascal_row(n-1)) + [1]
    '''since every pascal row has one in the front and one at the end
    you add [1] to both ends of the list. in between you output the sum of the
    adjacent terms of the row before'''

print (pascal_row(0))


def pascal_triangle (n):
    '''takes a single integer n and returns the list of lists 
    containing the values of all the rows up to and including n'''
    if n == 0:
        return [[1]]
    '''base case'''
    return  pascal_triangle(n-1) + [pascal_row(n)]
    '''outputs the list of the recursive of the previous pascal rows and adds
    it to the pascal row function for that specific row.'''

print (pascal_triangle(0))






