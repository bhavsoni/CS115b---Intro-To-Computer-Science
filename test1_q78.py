'''
CS 115 A, Spring 2017 - Test 1, Questions 7 and 8

Author: Bhavin Soni
Pledge: I pledge my honor that I have abided by the Stevens Honor System
'''
from cs115 import filter
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' RULES: You can use Canvas to download this file and upload your solution.
' You can use Eclipse to edit and run your program.  You should NOT look at
' other programs in Eclipse, you should NOT use any other programs, and you
' should NOT use any notes or books.
' According to the Honor Code, you should report any student who appears
' to be violating these rules.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Question 7 (20 points)
' Implement these functions using recursion.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def keep_integers(lst):
    '''Assume lst is a list of all different data types. There could be ints,
    floats, strings, booleans, nested lists, and more.
    Return a list of only the integers present in the original list. You do
    not have to worry about integers inside nested lists and can safely
    ignore them.
    You may use type(data) == int to determine if the data variable is an
    integer.
    This part is worth 20 points.'''
    if lst == []:
        return []
    elif type(lst[0]) == int:
        return [lst[0]] + keep_integers(lst[1:])
    else:
        return keep_integers(lst[1:])

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Question 8 (10 points)
' Implement this function using the Python's built-in 'filter' and 'lambda'.
' DO NOT USE recursion.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def keep_integers_filter(lst):
    '''Assume lst is a list of all different data types. There could be ints,
    floats, strings, booleans, nested lists, and more.
    Return a list of only the integers present in the original list. You do
    not have to worry about integers inside nested lists and can safely
    ignore them.
    You may use type(data) == int to determine if the data variable is an
    integer.
    This part is worth 10 points.'''
    return filter(lambda x: type(x) == int, lst)




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
            print('Test %d failed: %s(\'%s\') should be \'%s\'.' %
                  (test_num, function.__name__, arg, expected_output))
            print('   -- Received \'%s\'.' % received)
        else:
            print('Test %d failed: %s(%s) should be %s.' %
                  (test_num, function.__name__, arg, expected_output))
            print('   -- Received %s.' % received)

test(1, keep_integers, [], [])
test(2, keep_integers, [4, 2, 0], [4, 2, 0])
test(3, keep_integers, [4.3, 2.9, 0.0], [])
test(4, keep_integers, ['hi', [2, 3, 4], 1, 5, -6, False], [1, 5, -6])
test(5, keep_integers, [0, ['hi', [2, 3, 4]], 2.2, 2, True, 'True', 6], [0, 2, 6])
test(6, keep_integers_filter, [], [])
test(7, keep_integers_filter, [4, 2, 0], [4, 2, 0])
test(8, keep_integers_filter, [4.3, 2.9, 0.0], [])
test(9, keep_integers_filter, ['hi', [2, 3, 4], 1, 5, -6, False], [1, 5, -6])
test(10, keep_integers_filter, [0, ['hi', [2, 3, 4]], 2.2, 2, True, 'True', 6], [0, 2, 6])