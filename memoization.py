'''
Created on Feb 22, 2015
Last modified on Feb 26, 2016

@author: Brian Borowski

CS115 - Memoization
'''
import time

def LCS(S1, S2):
    '''Returns the length of the long common subsequence in strings S1 and S2.
    '''
    if S1 == '' or S2 == '':
        return 0
    if S1[0] == S2[0]:
        return 1 + LCS(S1[1:], S2[1:])
    return max(LCS(S1, S2[1:]), LCS(S1[1:], S2))

def fast_LCS(S1, S2):
    '''Returns the length of the long common subsequence in strings S1 and S2.
    Uses memoization to improve performance.'''
    def fast_LCS_helper(S1, S2, memo):
        # If key exists, return value already associated with key.
        if (S1, S2) in memo:
            return memo[(S1, S2)]

        # Do work.
        if S1 == '' or S2 == '':
            result = 0
        elif S1[0] == S2[0]:
            result = 1 + fast_LCS_helper(S1[1:], S2[1:], memo)
        else:
            result = max(fast_LCS_helper(S1, S2[1:], memo),
                         fast_LCS_helper(S1[1:], S2, memo))

        # Store and return result.
        memo[(S1, S2)] = result
        return result

    return fast_LCS_helper(S1, S2, {})

def LCS_with_values(S1, S2):
    '''Returns the length of the long common subsequence in strings S1 and S2
    as well as the characters common to S1 and S2.'''
    if S1 == '' or S2 == '':
        return (0, '')
    if S1[0] == S2[0]:  # Do the first symbols match
        result = LCS_with_values(S1[1:], S2[1:])
        return (1 + result[0], S1[0] + result[1])
    use_s1 = LCS_with_values(S1, S2[1:])
    use_s2 = LCS_with_values(S1[1:], S2)
    if use_s1[0] > use_s2[0]:
        return use_s1
    return use_s2

def fast_LCS_with_values(S1, S2):
    '''Returns the length of the long common subsequence in strings S1 and S2
    as well as the characters common to S1 and S2.
    Uses memoization to improve performance.'''
    def fast_LCS_helper(S1, S2, memo):
        # If key exists, return value already associated with key.
        if (S1, S2) in memo:
            return memo[(S1, S2)]

        # Do work.
        if S1 == '' or S2 == '':
            result = (0, '')
        elif S1[0] == S2[0]:
            lose_both = fast_LCS_helper(S1[1:], S2[1:], memo)
            result = (1 + lose_both[0], S1[0] + lose_both[1])
        else:
            use_s1 = fast_LCS_helper(S1, S2[1:], memo)
            use_s2 = fast_LCS_helper(S1[1:], S2, memo)
            if use_s1[0] > use_s2[0]:
                result = use_s1
            else:
                result = use_s2

        # Store and return result.
        memo[(S1, S2)] = result
        return result

    return fast_LCS_helper(S1, S2, {})

start_time = time.time()

# This function call may take up to ~30 seconds.
print(LCS_with_values('SUPERMARDEFKET', 'BOSTONXYZMARKET'))
print('Computation time without memoization:', time.time() - start_time, 'seconds')

start_time = time.time()
print(fast_LCS_with_values('SUPERMARDEFKET', 'BOSTONXYZMARKET'))
print('Computation time with memoization:', time.time() - start_time, 'seconds')
