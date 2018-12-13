'''
Created on Jan 31, 2017

@author: BhavinSoni
'''
from cs115 import map, reduce, range 
import string


def factorial (n):
    if n== 0:
        return 1
    return n * factorial(n-1)

'''print (factorial(4))'''

"""the base case is when the output of a given input is known without the need for
recursion. a recursive call is when a function calls itself. the 
argument(s) should gradually be approaching the base case == inductive definition/step"""

"""every time a  function is a called a stock frames contains 
information needed by the function such as all local variables. 
The action of placing the stock frame on the stock is called the 
push operation"""


def tower(n):
    if n==0:
        return 1
    return 2**tower(n-1)
   

def tower_reduce(c):
    def power (x,y):
        return y**x    
    return reduce(power,[2]*c)



def length(lst):
    if lst ==[]:
        return 0
    return 1+ length(lst[1:])

'''print (length([1,2,3,4]))'''

def reverse(lst):
    if lst == []:
        return []
    return reverse(lst[1:])+[lst[0]]


def sieve(L):
    if L==[]:
        return []
    else:
        return [L[0]]+ filter(lambda X: X%L[0] != 0, L[1:])

'''print (sieve [2,3,4,5,6,7,8,9])'''

def primes(n):
    return sieve(range(2,n+1))

def fib(n):
    if n<=1:
        return n 
    return fib(n-2)+fib(n-1)

'''tree recursion is when the pending 
operation of a recursion call implies making another 
recursive call'''

print (fib(4))


'''the power set of a set is the set of all its subsets
[1,2,3]
[[],[1],[2],[3],[1,2],[1,3], [2,3], [1,2,3]]

If a set has n elements there are 2^n subsets'''

def powerset(lst):
    if lst==[]:
        return [[]]
    lose_it = powerset(lst[1:])
    use_it=map(lambda subset: [lst[0]]+subset, lose_it)
    return lose_it+use_it


def subset (target,lst):
    if target ==0:
        return True
    if lst ==[]:
        return False
    '''use_it = subset(target-lst[0], lst[1:])
    lose_it = subset(target, lst[1:])
    return use_it or lose_it'''
    #omptimization for a list containing nonnegative values
    if lst[0]>target:
        return subset(target, lst[1:])
    return subset(target - lst[0], lst[1:]) or subset(target,lst[1:])

    
def subset_with_values(target,lst):
    if target ==0:
        return (True, [])
    if lst == []:
        return (False, [])
    use_it=subset_with_values(target - lst[0], lst[1:])
    if use_it[0]:
        return (use_it[0],[lst[0]]+use_it[1] )
    return subset_with_values(target, lst[1:])

#print (subset_with_values(12,[2,3,4,7,10,42]))


def maxmoney(coins):
    '''find the max amount of money from list of coins but 
    the two coins cannot be next to each other'''
    if coins ==[]:
        return 0
    useit = coins[0] + maxmoney(coins[2:])
    loseit = maxmoney(coins[1:])
    return max(useit, loseit)
    '''return max(coins[0] + maxmoney(coins[2:]), maxmoney(coins[1:]))'''

#print (maxmoney([5,10,1,2]))

def maxmoneyvalue(coins):
    '''same thing as above but return the list 
    of coins that make up that amount'''
    if coins==[]:
        return (0,[])
    useit= maxmoneyvalue(coins[2:])
    '''cant add 5+(0,[]) cant add number to a tuple'''
    newSum = coins[0] + useit[0]
    '''useit[0] has the value to add to tuple'''
    loseit= maxmoneyvalue(coins[1:])
    if newSum > loseit[0]:
        return (newSum, [coins[0]] + useit[1])
        '''you put the newSum into the list if the newSum is > than the loseit sum'''
        '''trying to add a list to list--> need to listify the coins[0]'''
    return loseit

''' newSum>loseit[0] basically maximizes it
the useit[0] basically adds it up--> sums it'''

#print (maxmoneyvalue([5,10,1,2]))

'''LCS --> longest common subsequence of a string
suuper - uber --> LCS = u e r = 3'''

def LCS(S1,S2):
    if S1 =='' or S2 =='':
        return 0
    if S1[0] == S2[0]:
        return 1+ LCS(S1[1:], S2[1:])
        '''without adding 1 the the recursive will always return 0'''
    return max(LCS(S1, S2[1:]), LCS(S1[1:], S2))

#print (LCS('gangster', 'gang'))

def lcsvalue (s1,s2):
    '''returns the length of the longest common subsequence 
    in string 1 and string 2 and as well as the string of 
    the common characters.the result will be a tuple'''
    if s1 == '' or s2 == '':
        return [0,'']
    if s1[0] == s2[0]:
        result = lcsvalue(s1[1:], s2[1:])
        '''result is a tuple'''
        return (1 + result[0], s1[0] + result[1])
        '''lcsvlaue return a tuple but you cant add a number 
        into so you add tuple[0] so you can add the element into it.
        want to cacavenate the s1[0]'''
        '''s1[0] want to return the length and the character of the string
        and s1 = s2 so we just need s1'''
    useS1 = lcsvalue(s1, s2[1:])
    useS2 = lcsvalue(s1[1:], s2)
    '''s1 and s2 bring 2 tuples respectively. compare the two to
    the longer length of the tuple'''
    if useS1[0] > useS2[0]:
        return useS1
    return useS2
    '''return max(useS1[0], useS2[0]) after useS2 doesnt work because you just returned a int,int
    and not an int, tuple'''

#print (lcsvalue('ofoefqofq', 'vnovqoienwvo'))

def distance (first, second):
    if first == '':
        return len(second)
    if second == '':
        return len(first)
    if first[0] == second[0]:
        return distance(first[1:], second[1:])
    substitution = distance(first[1:], second[1:])
    '''substituiton is counted as one word so you add the 1 so it can be counted'''
    deletion =  distance (first[1:], second)
    insertion = distance(first, second[1:])
    return 1+ min(substitution, deletion, insertion)

#print (distance ('sam', 'spot'))



'''**********MEMOIZAITON********'''
def fib1 (n):
    if n<= 1:
        return n
    return fib1(n-1) + fib1(n-2)

#print (fib1 (3))

'''for i in range(40):
    print (i, fib(i))'''
    
'''Step 1) if key is in dictionary, return value associated with key. 

    Step 2)do work! make recursive calls and store the value in a local 
    variable 
    
    Step 3) store the result in the dictionary and return the result'''
    
def fibMemo (n):
    def fibHelper(n, memo):
            if n in memo:
                return memo[n]
            '''step 1'''
            if n<= 1:
                result = n
            else:
                result = fibHelper(n-1, memo) + fibHelper(n-2, memo)
            '''step 2'''
            memo[n] = result
            return result
    return fibHelper(n, {})

'''for i in range (41):
    print(i, fibMemo(i))'''
#print (fibMemo(40))



'''EXAM 1 SHIT
need to know the types of recursion

n factorial  = linear recursion =  n*factorial(n-1)

process in the fall practice test  = linear = bc you have to go 
back up tp get the answer 

tree recusrion = 2 or more recursive call 

lst = [1,4,2,3,5,9,8]
keep the evens
filter(lambda x: x%2 == 0, lst)

filter keeps '''

def fast_LCS(S1,S2):
    def LCShelper (S1, S2, memo):
        if (S1, S2) in memo:
            return memo[(S1,S2)]
        
        if S1 =='' or S2 =='':
            return 0
        elif S1[0] == S2[0]:
            result =  1 + LCShelper(S1[1:], S2[1:], memo)
            '''without adding 1 the the recursive will always return 0'''
        else: 
            result = max(LCShelper(S1, S2[1:], memo), LCShelper(S1[1:], S2, memo))
        memo [(S1, S2)] = result
        return result
    return LCShelper(S1, S2, {})

#print (fast_LCS('fewfnigerigbrigubwivwiu', 'enoewuegnigbreiugipwvweovevpewpvubepeuibv'))



def lcsvaluefast (s1,s2):
    def lcshelper (s1,s2,memo):
        if (s1, s2) in memo:
            return memo[(s1,s2)]
        
        if s1 == '' or s2 == '':
            result =  (0,'')
        elif s1[0] == s2[0]:
            lose_both = lcshelper(s1[1:], s2[1:], memo)
            result = (1 + lose_both[0], s1[0] + lose_both[1])
        else:
            useS1 = lcshelper(s1, s2[1:], memo)
            useS2 = lcshelper(s1[1:], s2, memo)
            if useS1[0] > useS2[0]:
                result = useS1
            else:
                result = useS2
        
        memo[(s1,s2)] = result
        return result
    return lcshelper(s1,s2,{})

#print (lcsvaluefast('eofhewgbiugbeibeivbeivbewuvibewivubeivbwivbeivbwe', 'wiiebceuivbweuvbewpuvbpewbvuepvbeiubvepivbev'))


def reverse0(s):
    if s == '':
        return ''
    return reverse[1:] + s[0]

def keep_palindromes(lst):     
    '''Assume lst is a list of strings where all letters are lower case.     
    Return a list of strings that are palindromes. A palindrome is a word     
    that has the same spelling both forward and backward. For instance,     
    'racecar' is a palindrome. You may use the reverse function written     
    above.''' 
    if lst == []:
        return []
    if lst[0] == reverse[0]:
        return [lst[0]] + keep_palindromes(lst[1:])
    return keep_palindromes(lst[1:])

def keep_palindromes_filter(lst):
    return filter(lambda x: x == reverse(x), lst)

def zippy(l,m):
    if l == [] or m == []:
        return []
    return [[l[0], m[0]]] + zippy(l[1:],m[1:])

print (zippy([1,2,3], ['a','b','c']))

    
def removepunct (str):
    if str == '':
        return ''
    def remove(x, L):
        if x == L[0]:
            return L[1:]
        else:
            return remove(x, L[1:])
    return 

    
''''''''''''''''''''''logisim''''''''''''
S-R Latch 
    a bistable multivibrator with two stable output states
    
    Q=1 then notQ=0 is set
    Q=0 then notQ=1 is reset
    
    if if both Q and notQ are the same = state invalid
    activation of S sets circuits
    activation of R resets circuit
    activation of both S and R is invalid circuit

D-latch
    1-bit memory circuit
    store/lacthes one to a 'high' or low state when disabled
    reads neew data from the D input when enabled 
    
    D    strobe    Q
    
    x      0       Q
    1      1       1
    0      1       0
               
    where x = dont care about value      
    
'''
   
