'''
CS 115 A, Spring 2017 - Test 2, Questions 7 and 8

Author: Bhavin Soni
Pledge: I pledge my honor that I have abided by the Stevens Honor System
'''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' RULES: You can use Canvas to download this file and upload your solution.
' You can use Eclipse to edit and run your program. You should NOT look at
' other programs in Eclipse, you should NOT use any other programs, and you
' should NOT use any notes or books.
' According to the Honor Code, you should report any student who appears
' to be violating these rules.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Question 7 (10 points)
' Implement this function using recursion.
' Tribonacci numbers follow a pattern similar to Fibonacci numbers, except
' that the next number in the sequence is the sum of the previos three
' numbers.
' The sequence is as follows: 0, 0, 1, 1, 2, 4, 7, 13, 24, 44, ...
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def tribonacci(n):
    '''Returns the nth Tribonacci number. The 0th number is 0, the 1st number
    is 0, the 2nd number is 1, and any number beyond that is the sum of the
    previous three numbers.
    Examples:
    tribonacci(0) -> 0
    tribonacci(2) -> 1
    tribonacci(5) -> 4'''
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Question 8 (20 points)
' Implement this function using recursion AND memoization.
' Tribonacci numbers follow a pattern similar to Fibonacci numbers, except
' that the next number in the sequence is the sum of the previos three
' numbers.
' The sequence is as follows: 0, 0, 1, 1, 2, 4, 7, 13, 24, 44, ...
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def trib_memo(n):
    '''Returns the nth Tribonacci number. The 0th number is 0, the 1st number
    is 0, the 2nd number is 1, and any number beyond that is the sum of the
    previous three numbers. Uses memoization to improve performance.'''
    def tribfast(n, memo):
        if n in memo:
            return memo[n]
        elif n <= 1:
            result = 0
        elif n == 2:
            result = 1
        else:
            result = tribfast(n-1, memo) + tribfast(n-2, memo) + tribfast(n-3, memo)
        
        memo[n] = result
        return result 
    
    return tribfast (n, {})

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Code to test your work. DO NOT TOUCH.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def test(test_num, function, arg, expected_output):
    received = function(arg)
    try:
        assert(received == expected_output)
        print('Test %d passed.' % test_num)
    except:
        if isinstance(arg, str):
            print('Test %d failed: %s(\'%s\') should be %s.' %
                  (test_num, function.__name__, arg, expected_output))
            print('   -- Received %s.' % received)
        else:
            print('Test %d failed: %s(%s) should be %s.' %
                  (test_num, function.__name__, arg, expected_output))
            print('   -- Received %s.' % received)

test(1, tribonacci, 0, 0)
test(2, tribonacci, 1, 0)
test(3, tribonacci, 2, 1)
test(4, tribonacci, 3, 1)
test(5, tribonacci, 4, 2)
test(6, tribonacci, 7, 13)
test(7, tribonacci, 9, 44)
test(8, tribonacci, 10, 81)
test(9, tribonacci, 11, 149)
test(10, tribonacci, 12, 274)

test(11, trib_memo, 0, 0)
test(12, trib_memo, 1, 0)
test(13, trib_memo, 2, 1)
test(14, trib_memo, 3, 1)
test(15, trib_memo, 4, 2)
test(16, trib_memo, 7, 13)
# If you memoize correctly, these function calls will return nearly
# instantaneously.
test(17, trib_memo, 30, 15902591)
test(18, trib_memo, 49, 1697490356184)
test(19, trib_memo, 50, 3122171529233)
test(20, trib_memo, 60, 1383410902447554)
