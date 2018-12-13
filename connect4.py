'''
Created on May 1, 2017

@author: BhavinSoni
'''
class Board(object):
    #initialize variables and the board is preset with the dimensions if not specified
    def __init__(self, width=7, height=6):
        self.width = width
        self.height = height
        self.board = [[' ' for x in range(self.width)] for y in range(self.height)]
        #creates the board matrix
        
    def __str__(self):
        '''returns a string (it does not print a string) representing the Board object that calls it.'''
        a = '|'     #make variable straight slash
        for row in range(self.height):
            for col in range(self.width):       
                a = a + self.board[row][col] + '|'      #adds the straight slash and space on the matrix and adds another slash making part of the cell/spot
            a = a +"\n|"    #adds the slash to new space on matrix but then ends the line to add slash to next line 
        a = a[:-1] #placed here so subtract the extra slash made 
        a += '-' * 15 +'\n' #adds ----- to the bottom of the board
        for i in range(0,self.width): 
            a += ' ' + str(i) #prints the numbers of columns as stings separated by spaces
        return a #returns the board

    def allowsMove(self, col):
        '''this method should check to be sure that c is within the range from 0 to the last column and make sure that there is still room left in the column!'''
        if self.board[0][col] != ' ': 
            return False #if theres not an empty space return false
        if col < 0 or col + 1 > self.width: #if the col is less than zero or greater than the width then return false
            return False
        return True
    
    def addMove(self, col, ox):
        '''This method should add an ox checker, where ox is a variable holding a string that is either "X" or "O", into column col.'''
        for row in range(self.height-1, -1, -1): #checks from the bottom up so in reverse
            if self.board[row][col] == ' ': 
                self.board[row][col] = ox  #if the space is empty ox is the checker
                break 
    
    def setBoard( self, moveString ):
        """ takes in a string of columns and places
            alternating checkers in those columns,
            starting with 'X'
            For example, call b.setBoard('012345')
            to see 'X's and 'O's alternate on the
            bottom row, or b.setBoard('000000') to
            see them alternate in the left column.
            moveString must be a string of integers
        """
        nextCh = 'X'   # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove(col, nextCh)
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'
    
    def delMove(self, col): 
        '''method should do the "opposite" of addMove. That is, it should remove the top checker from the column col.'''
        for row in range(self.height): #checks from the top to the bottom opposite of the add move
            if self.board[row][col] != ' ': # if the space isnt empty it will become empty
                self.board[row][col] = ' '
                break
    
    
    def winsFor(self, ox):
        b = self.board
        
        #horizontal win
        for row in range(self.height):
            for col in range(self.width - 3): #width -3 because we need a range of 4 spaces horizontally
                if b[row][col] == b[row][col + 1] == b[row][col + 2] == b[row][col + 3] == ox: 
                    return True #if the spaces side by side are equivalent to the o or x spot then we have win
        
        #column win 
        for row in range(self.height - 3): # this time we need 4 on top of each other so we need a height of 4
            for col in range(self.width):
                if b[row][col] == b[row + 1][col] == b[row + 2][col] == b[row + 3][col] == ox:
                    return True #if the spaces on top of each other in the board are equivalent to either o or x then we have a win
    
        #diagonal win
        b = self.board
        for row in range(self.height - 3): # diagonal bottom left to top right so we need 4 rows and 4 columns 
            for col in range(self.width - 3):
                if b[row][col] == b[row + 1][col + 1] == b[row + 2][col + 2] == b[row + 3][col + 3] == ox:
                    return True #if the the x or o are equivalent in each of the diagonal direction where the row increases by one space and the column increases by one space then we have a win
    
        #diagonal 2 win
        for row in range(self.height - 1, 2, -1): #diagonal form the top left to bottom right we need to decrese negitavely from the top to the bottom
            for col in range(self.width - 3): #need 4 columns
                if b[row][col] == b[row - 1][col + 1] == b[row - 2][col + 2] == b[row - 3][col + 3] == ox:
                    return True #decrese row by one and increase column by 1 making the diagonal pattern and if its equivalent to either x or o we have a win
        
        return False


    def hostGame (self) :
        print ("Welcome to Connect Four")
        print (self) #prints the board
        while True:
            turn = -1 #set the turn to -1 for now so we can check with the while loop.
            while self.allowsMove(int(turn)) == False: #while there are enough spaces in the col for x let the user input the spot for x if there are not enough spaces the while loop breaks and has the user repeatedly input for x
                turn = int(input("X's Turn: ")) #the user can in put where they want to place X
            self.addMove(turn, "X") # X is placed in the column where the user has indicated
            print (self) #prints the board
            if self.winsFor("X") : #if X is the ox in any of the win strategies defined above then x wins 
                print ("X Wins!") 
                return #returns nothing and the game is done 
            
            turn = -1 #do the exact same thing did above for X but for O now
            while self.allowsMove(int(turn)) == False:
                turn = int(input("O's turn: "))
            self.addMove(turn, "O")
            print (self)
            if self.winsFor("O") :
                print ("O Wins!")
                return 


b = Board(7,6)
b.hostGame()
        

    