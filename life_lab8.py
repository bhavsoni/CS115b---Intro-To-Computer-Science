#
# life.py - Game of Life lab
#
# Name:Bhavin Soni
# Pledge: I pledge my honor that I have abided by the Stevens Honor System
#

import random
import sys

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    """ returns a 2d array with "height" rows and "width" cols """ 
    A = []
    for row in range(height):
        A += [createOneRow(width)]
    return A

def printBoard( A ):
    """ this function prints the 2d list-of-lists
        A without spaces (using sys.stdout.write)
    """
    for row in A:
        for col in row:
            sys.stdout.write( str(col) )
        sys.stdout.write( '\n' )
        
def diagonalize(width,height):
    """ creates an empty board and then modifies it
        so that it has a diagonal strip of "on" cells.
    """
    A = createBoard( width, height )
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

def innerCells(w,h):
    '''returns a 2d array of all live cells - with the value of 1 - 
    except for a one-cell-wide border of empty cells (with the value of 0) 
    around the edge of the 2d array
    '''
    A = createBoard(w,h)
    for row in range(h):
        for col in range(w):
            if (0 < row < h-1) and (0 < col < w-1):
                A[row][col] = 1
    return A

#A = innerCells(5,5)
#print (printBoard (A))

def randomCells(w,h):
    '''returns an array of randomly-assigned 1's and 0's except 
    that the outer edge of the array is still completely empty (all 0's) as 
    in the case ofinnerCells
    '''
    A = createBoard(w,h)
    for row in range(h):
        for col in range(w):
            if (0 < row < h-1) and (0 < col < w-1):
                A[row][col] = random.choice([0,1])
    return A

#A = randomCells(10,10)
#print (printBoard (A))

def copy(A):
    '''makes a deep copy of the 2d array A.  takes in a 2d array A and it will
     output a new 2d array of data that has the same pattern as the input array.'''
    B = createBoard(len(A),len(A[0]))
    h = len(A)
    w = len(A[0])
    for row in range(h):
        for col in range(w):
            B[row][col] = A[row][col]
    return B

#oldA = createBoard(2,2)
#print (printBoard(oldA))

#newA = copy(oldA)
#print (printBoard(newA))

#oldA[0][0]=1
#print (printBoard(oldA))

#print(printBoard(newA))


def innerReverse(A):
    '''takes an old 2d array (or "generation") and then creates a 
    new generation of the same shape and size 
    (either with copy, above, or createBoard)'''
    B = createBoard(len(A),len(A[0]))
    h = range(1,(len(A)-1))
    w = range(1,(len(A[0])-1))
    for row in h:
        for col in w:
            if(A[row][col]) == 0:
                (B[row][col]) = 1
            else:
                (B[row][col]) = 0
    return B

#A = randomCells(8,8)
#print (printBoard(A))

#b = innerReverse(A)
#print (printBoard(b))

def countNeighbors (row, col, A):
    '''returns the number of live neighbors for a cell in the board A at a particular row and col'''
    counter = 0
    for x in range(-1, 2, 1):
        for y in range(-1, 2, 1):
            if abs(x) + abs(y) != 0:
                counter += A[row+x][col+y]
    return counter


def next_life_generation(A):
    """ makes a copy of A and then advanced one
        generation of Conway's game of life within
        the *inner cells* of that copy.
        The outer edge always stays 0.
    """
    B = createBoard(len(A),len(A[0]))
    rangeHeight = range(1,(len(A)-1))
    rangeWidth = range(1,(len(A[0])-1))
    for row in rangeHeight:
        for col in rangeWidth:
            if countNeighbors(row,col,A) < 2:
                B[row][col] = 0
            elif countNeighbors(row,col,A) > 3:
                B[row][col] = 0
            elif A[row][col] == 0 and countNeighbors(row,col,A) == 3:
                B[row][col] = 1
            else:
                B[row][col] = A[row][col]
    return B

A = [ [0,0,0,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,0,0,0]]

print (printBoard(A))

#A2 = next_life_generation( A )
#print (printBoard (A2))

#A3 = next_life_generation( A2 )
#print (printBoard (A3))