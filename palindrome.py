'''
Created on May 2, 2017

@author: BhavinSoni
'''
import sys
class Stack(object):
    def __init__(self):
        self.__items = []
        
    def isEmpty(self):
        return self.__items == []
    
    def push(self,item):
        self._items.append(item)
        
    def pop(self):
        '''remove from the top of the stack and returns it'''
        return self.__items.pop()
    
    def peek(self):
        return self.__items[-1]
    
    def size(self):
        return len(self.__items)
    
def isPalindorme(s):
    s = s.lower()
    stack = Stack()
    for i in s:
        stack.push(i)
    for i in s:
        s_char = stack.pop()
        if s_char != i:
            return False
            print ('not a palindrome')
    return True
    print('palindrome')
    
if __name__=="__main__":
    if len(sys.argv) != 2:
        print('Usage: '+ sys.argv[0] + ' <string>')
        sys.exit(1)
    print('string: ' + sys.argv[1])
    print(isPalindorme(sys.argv[1]))
    sys.exit(0)