'''
Created on Feb 1, 2017
Bhavin Soni
#I pledge my honor that iI have abided by the Stevens honor system
@author: BhavinSoni
'''


def dot (L,K):
    if L==[] or K==[]:
        return 0
    else:
        return L[0]*K[0] + dot(L[1:],K[1:])

print (dot([5,3], [6,4]))


def explode (S): 
    if S=="":
        return []
    else:
        return [S[0]]+explode(S[1:])
        
print (explode('hello'))



def ind(e,L):
    if L==[] or L=='':
        return 0
    if e==L[0]:
        return 0
    else:
        return 1 + ind(e,L[1:])

print (ind(3, [1,2,3,4]))


def removeAll (e,L):
    if L==[]:
        return []
    if e==L[0]:
        return removeAll(e,L[1:])
    else:
        return [L[0]] + removeAll(e,L[1:])

print(removeAll(42,[55,77,42,11,42,88]))


def myFilter(f,L):
    if L==[]:
        return []
    if f(L[0]) == True:
        return [L[0]]+ myFilter(f,L[1:])
    else:
        return myFilter(f,L[1:])
    
        
def deepReverse(L):
    if L==[]:
        return []
    elif isinstance (L[0], list):
        return deepReverse(L[1:]) + [deepReverse(L[0])]
    else:
        return deepReverse(L[1:])+[L[0]]
    
print (deepReverse([1,[2,3],4]))