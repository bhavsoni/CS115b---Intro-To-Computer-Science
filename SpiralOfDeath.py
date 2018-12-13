'''
Created on Feb 16, 2017

@author: BhavinSoni
'''
import turtle
from test.datetimetester import pairs

def squareSpiral(walls):
    def squareSpiralHelper(distance, initial, count):
        '''base case is the when the recusrion stop. when counts = number of walls it will stop
        no return is needed because it doesnt have to return anything of value'''
        if count == walls:
            turtle.done()
            '''the turtle is done running/stops'''
        else:
            '''if we keep making left hand turns so we need to simplify it by making turn 90 to the left'''
            turtle.left(90)
            turtle.forward(distance)
            squareSpiralHelper(distance + initial * (count % 2), initial, count + 1)
            '''everytime you have an odd count number the initial is inceased by 20
            (20,20,0) --> (20,20,1) ---> (40,20,2)--> (40,20,3) ---> (60,20,4) ---> etc.'''
            
    squareSpiralHelper(20, 20, 0)

squareSpiral(30)


'''dictionary is a hash table or associative array that contains key value pairs. msps values to keys'''