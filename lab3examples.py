from cs115 import map, range, reduce

def mystery1(n):
    return m_help(n, 0)

def m_help(n, r):
    if n == 0:
        return r
    print(n, r)
    return m_help(n//10, r*10 + n%10)

##print("n  ", "r")
##print(mystery(452))


def member(x, L):
    if L == []:
        return False
    if x == L[0]:
        return True
    else:
        return member(x, L[1:])

##print(member(42, [1 , 3, 5, 42, 7]))
##print(member(42, ["spam", "is", "yummy", 2]))

def even(x):
    return x % 2 == 0

##print(filter(even, range(100)))

def mystery(item, L):
    NewL = map(lambda x: x == item, L)
    return sum(NewL) > 0

##print(mystery(5, [1, 2, 5, 8, 5, 3]))

def powerset(L):
    if L == []:
        return [[]]
    else:
        loseIt = powerset(L[1:])
        useIt = map(lambda item: [L[0]] + item, loseIt)
        return useIt + loseIt

##print(powerset([1, 2]))
##print(powerset([1, 2, 3]))

def subset(target, L):
    if target == 0:
        return True
    elif L == []:
        return False
    elif L[0] > target:
        return subset(target, L[1:])
    else:
        useIt = subset(target - L[0], L[1:])
        loseIt = subset(target, L[1:])
        return useIt or loseIt

print(subset(12, [2, 3, 4, 7, 10, 42]))
print(subset(8, [2, 3, 4, 7, 10, 42]))

def LCS(S1, S2):
    """returns the longest common substring bewteen two strings"""
    if S1 == "" or S2 == "":
        return 0
    if S1[0] == S2[0]:
        return 1 + LCS(S1[1:], S2[1:])
    else:
        return max(LCS(S1[1:], S2), LCS(S1, S2[1:]))
    

def knapsack(capacity, items):
    if items == [] or capacity == 0:
        return 0
    if items[0][0] > capacity:
        return knapsack(capacity, items[1:])
    else:
        useIt = items[0][1] + knapsack(capacity - items[0][0], items[1:])
        loseIt = knapsack(capacity, items[1:])
        return max(useIt, loseIt)

print(knapsack(7, [[2, 100], [3, 112], [4, 125]]))

def primes(n):
    def sieve(lst):
        if lst == []:
            return []
        return [lst[0]] + sieve(filter(lambda x: x % lst[0] != 0, lst[1:]))
    return sieve(range(2, n + 1))

def power_tail(x, y):
    def power_tail_helper(x, y, accum):
        if y == 0:
            return accum
        return power_tail_helper(x, y - 1, accum * x)
    return power_tail_helper(x, y, 1)
