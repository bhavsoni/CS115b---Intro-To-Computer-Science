'''
Created on Feb 1, 2015
Last modified on Jan 23, 2016

@author: Brian Borowski

CS115 - Recursion
'''
import math
from cs115 import map, reduce, filter

def factorial(n):
    '''Computes n!'''
    if n == 0:
        return 1
    return n * factorial(n - 1)

def tower(n):
    '''Computes 2^(2^(2)) with n twos, using recursion.'''
    if n == 0:
        return 1
    return 2 ** tower(n - 1)

def tower_reduce(n):
    '''Computes 2^(2^(2)) with n twos, using reduce.'''
    def power(x, y):
        return y ** x
    return reduce(power, [2] * n)

def length(lst):
    '''Returns the length of the list.'''
    if lst == []:
        return 0
    return 1 + length(lst[1:])

def reverse(lst):
    '''Takes as input a list of elements and returns the list in reverse order.
    '''
    if lst == []:
        return []
    return reverse(lst[1:]) + [lst[0]]

def member(x, lst):
    '''Returns True if x is contained in the list and False otherwise.'''
    if lst == []:
        return False
    if x == lst[0]:
        return True
    return member(x, lst[1:])

def collapse(lst):
    '''Collapses a list of possibly nested lists into a single list of values.
    '''
    if lst == []:
        return []
    if isinstance(lst[0], list):
        return collapse(lst[0]) + collapse(lst[1:])
    return [lst[0]] + collapse(lst[1:])

def power_tail(x, y):
    '''Computes x^y with tail recursion.'''
    def power_tail_helper(x, y, accum):
        if y == 0:
            return accum
        return power_tail_helper(x, y - 1, accum * x)

    return power_tail_helper(x, y, 1)

def my_map(f, lst):
    '''Returns a new list where the function f has been applied to every element
    in the original list.'''
    if lst == []:
        return []
    return [f(lst[0])] + my_map(f, lst[1:])

def my_reduce(f, lst):
    '''Reduces the list to a single value as dictated by the predicate f.'''
    def my_reduce_helper(f, lst, accum):
        if lst == []:
            return accum
        return my_reduce_helper(f, lst[1:], f(accum, lst[0]))

    if lst == []:
        raise TypeError('my_reduce() of empty sequence with no initial value')
    return my_reduce_helper(f, lst[1:], lst[0])

def my_reduce2(f, lst):
    '''Reduces the list to a single value as dictated by the predicate f.'''
    if lst == []:
        raise TypeError('my_reduce2() of empty sequence with no initial value')
    if lst[:-1] == []:
        return lst[-1]
    return f(my_reduce2(f, lst[:-1]), lst[-1])

def my_reduce_wrong(f, lst):
    '''Reduces the list to a single value as dictated by the predicate f.'''
    if lst == []:
        raise TypeError(
                    'my_reduce_wrong() of empty sequence with no initial value')
    if lst[1:] == []:
        return lst[0]
    return f(lst[0], my_reduce_wrong(f, lst[1:]))

def dedupe(lst):
    '''Returns a list with no consecutive duplicate elements.'''
    if len(lst) <= 1:
        return lst
    if lst[0] == lst[1]:
        return dedupe(lst[1:])
    return [lst[0]] + dedupe(lst[1:])

def reverse_num(n):
    return reverse_helper(n, 0)

def reverse_helper(n, r):
    if n == 0:
        return r
    return reverse_helper(n / 10, r * 10 + n % 10)

def prime(n):
    '''Returns whether or not an integer is prime.'''
    possible_divisors = range(2, int(math.sqrt(n)) + 1)
    divisors = filter(lambda x: n % x == 0, possible_divisors)
    return len(divisors) == 0

def primes(n):
    '''Returns a list of primes in the range [2, n] computed via the sieve of
    Eratosthenes.'''
    def sieve(lst):
        if lst == []:
            return []
        return [lst[0]] + sieve(filter(lambda x: x % lst[0] != 0, lst[1:]))

    return sieve(range(2, n + 1))

def suffixes(L):
    '''Assume L is a list.
       Return the suffixes of L, in decreasing order by length.'''
    if L == []:
        return [[]]
    return [L] + suffixes(L[1:])

def prefixes(L):
    '''Assume L is a list.
       Return the prefixes of L, in increasing order by length.'''
    if L == []:
        return [[]]
    return prefixes(L[:-1]) + [L]

def num_digits(num):
    '''Assume num is a nonnegative integer.
    Returns the number of digits in num.
    Examples:
    num_digits(0) -> 1
    num_digits(9) -> 1
    num_digits(39) -> 2
    num_digits(1000) -> 4
    '''
    if num < 10:
        return 1
    return 1 + num_digits(num / 10)

def num_digits_all(lst):
    '''Assume lst is a list of nonnegative integers.
    Returns a list of 2-element lists (or pairs) where the first number
    is from lst and the second is the number of digits in the first.
    Examples:
    num_digits_all([]) -> []
    num_digits_all([21]) -> [[21, 2]]
    num_digits_all([1, 23, 546, 4]) -> [[1, 1], [23, 2], [546, 3], [4, 1]]

    Note: You MUST use map to get credit for this part.
    '''
    return map(lambda n: [n, num_digits(n)], lst)

print('factorial(5):', factorial(5))
print('tower(4):', tower(4))
print('tower_reduce(4):', tower_reduce(4))
print('reverse([1, 2, 3, 4]):', reverse([1, 2, 3, 4]))
print('length([1, 2, 3, 4]):', length([1, 2, 3, 4]))
print()
print(member(-1, [1, 3, 5, 2, 4, 6]))
print(collapse([1, [2, 3], [[4, 5], [6]], 7]))
print(my_map(lambda x : x * x, [1, 2, 3, 4, 5]))
print()
print(my_reduce(lambda x, y: x ** y, [1, 2, 3, 4]) == \
      my_reduce2(lambda x, y: x ** y, [1, 2, 3, 4]))
print(my_reduce(lambda x, y: x ** y, [1, 2, 3, 4]) == \
      my_reduce2(lambda x, y: x ** y, [1, 2, 3, 4]))
print(my_reduce(lambda x, y: x / y, [1.0, 2.0, 3.0, 4.0]) == \
      my_reduce2(lambda x, y: x / y, [1.0, 2.0, 3.0, 4.0]))
print(my_reduce(lambda x, y: x / y, [1.0, 2.0, 3.0, 4.0]) == \
      my_reduce_wrong(lambda x, y: x / y, [1.0, 2.0, 3.0, 4.0]))
print(my_reduce(lambda x, y: x + y, [1]) == \
      my_reduce2(lambda x, y: x + y, [1]))
print(my_reduce(lambda x, y: x + y, [1, 2]) == \
      my_reduce2(lambda x, y: x + y, [1, 2]))
print(my_reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]) == \
      my_reduce2(lambda x, y: x + y, [1, 2, 3, 4, 5]))
print()
print('Deduped:', dedupe([3, 4, 4, 9, 9, 2, 4]))
print('Deduped:', dedupe([1, 3, 3, 3, 5, 7]))
print('Reverse(452):', reverse_num(452))
print('Reverse(1):', reverse_num(1))
print('Reverse(26):', reverse_num(26))
print()
print('3^4:', power_tail(3, 4))
print('Primes up to 100:', primes(100))
print('suffixes([1, 2, 3, 4, 5]):', suffixes([1, 2, 3, 4, 5]))
print('prefixes([1, 2, 3, 4, 5]):', prefixes([1, 2, 3, 4, 5]))
print()
print(num_digits_all([1, 23, 546, 4]))