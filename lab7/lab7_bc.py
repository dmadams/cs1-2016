# B.1.1.
def union(s1, s2):
    '''Takes 2 sets as arguments and returns their union as another set.
    '''
    s = set([])
    for i in s1:
        s.add(i)
    for j in s2:
        s.add(j)
    return s

# B.1.2.
def intersection(s1, s2):
    '''Takes 2 sets as arguments and returns their intersection as another set.
    '''
    s = set([])
    for i in s1:
        for j in s2:
            if i == j:
                s.add(i)
    return s

# B.2.
def mySum(*nums):
    '''Takes an arbitrary number of arguments, all of which should be integers
    greater than zero, and returns their sum. Raises a TypeError if an argument
    is not an integer and a ValueError if an argument is <= 0.
    '''
    for i in nums:
        if type(i) != int:
            raise TypeError('All arguments must be of type int.')
        if i <= 0:
            raise ValueError('All arguments must be > 0.')
    x = 0
    for j in nums:
        x += j
    return x
        
# B.3.
def myNewSum(*nums):
    '''Takes a list or an arbitrary number of integers, but not both a list and
    integer arguments or multiple lists. All the elements within the lists
    should be integers greater than zero. Returns the sum of the list or of the
    integers. Raises a TypeError if there are multiple lists or a list and other
    arguments or an element or argument is not an integer and a ValueError if an
    element or argument is <= 0.
    '''
    if len(nums) == 0:
        return 0
    elif type(nums[0]) == list:
        if len(nums) > 1:
            raise TypeError('Will not accept a list and multiple elements '\
                            'or multiple lists.')
        for i in nums[0]:
            if type(i) != int:
                raise TypeError('All elements within list must be of type int.')
            if i <= 0:
                raise ValueError('All elements with list must be > 0.')
        x = 0
        for j in nums[0]:
            x += j
        return x
    
    for k in nums:
        if type(k) != int:
            raise TypeError('All arguments must be of type int.')
        if k <= 0:
            raise ValueError('All arguments must be > 0.')
    x = 0
    for l in nums:
        x += l
    return x

# B.4.
def myOpReduce(lst, **arg):
    if len(arg) == 0:
        raise ValueError('No keyword argument.')
    elif len(arg) > 1:
        raise ValueError('Too many keyword arguments.')
    elif 'op' not in arg.keys():
        raise ValueError('Invalid keyword argument.')    
    elif type(arg['op']) != str:
        raise TypeError('Value for keyword argument \'op\' must be a string.')
    elif arg['op'] not in ['+', '*', 'max']:
        raise ValueError('Invalid keyword argument.')    
    
    if arg['op'] == '+':
        x = 0
        for i in lst:
            x += i
        return x
    elif arg['op'] == '*':
        x = 1
        for i in lst:
            x *= i
        return x
    elif arg['op'] == 'max':
        if len(lst) == 0:
            return 0
        x = lst[0]
        for i in lst:
            if i > x:
                x = i
        return x

# C.1.
# It is not necessary to raise a KeyError, Python does this automatically. Also,
# in raising a KeyError it should not just quit.
import sys

def sum_of_key_values(dict, key1, key2):
    '''Return the sum of the values in the dictionary stored at key1 and key2.
    '''
    return dict[key1] + dict[key2]  

# C.2.
# It is not necessary to raise a KeyError, Python does this automatically.
import sys

def sum_of_key_values(dict, key1, key2):
    '''Return the sum of the values in the dictionary stored at key1 and key2.
    '''
    return dict[key1] + dict[key2]

# C.3. 
# It is not necessary to raise a KeyError, Python does this automatically.
import sys

def sum_of_key_values(dict, key1, key2):
    '''Return the sum of the values in the dictionary stored at key1 and key2.
    '''
    return dict[key1] + dict[key2]

# C.4.
# It is not necessary to raise a KeyError, Python does this automatically. Also,
# this is unnecessarily complex.
import sys

def sum_of_key_values(dict, key1, key2):
    '''Return the sum of the values in the dictionary stored at key1 and key2.
    '''
    return dict[key1] + dict[key2]

# C.5.
# The print statement is unnnecessary.
import sys

def fib(n):
    '''Return the nth fibonacci number.'''
    if n < 0:
        raise ValueError('n must be >= 0')
    elif n < 2:
        return n  # base cases: fib(0) = 0, fib(1) = 1.
    else:
        return fib(n-1) + fib(n-2)
    
# C.6.
# The error must be raised before the print statement. Also, the print statement
# is unnecessary.
import sys

def fib(n):
    '''Return the nth fibonacci number.'''
    if n < 0:
        raise ValueError('n must be >= 0')
    elif n < 2:
        return n  # base cases: fib(0) = 0, fib(1) = 1.
    else:
        return fib(n-1) + fib(n-2)

# C.7. 
# This error should be a ValueError not a TypeError.
from math import exp

def exp_x_over_x(x):
    '''
    Return the value of e**x / x, for x > 0.0 and
    e = 2.71828... (base of natural logarithms).
    '''
    if x <= 0.0:
        raise ValueError('x must be > 0.0')
    return (exp(x) / x)

# C.8.
# The Exceptions should be a TypeError and a ValueError respectively. Just
# raising an Exception is not specific enough.
from math import exp

def exp_x_over_x(x):
    '''
    Return the value of e**x / x, for x > 0.0 and
    e = 2.71828... (base of natural logarithms).
    '''
    if type(x) != float:
        raise TypeError('x must be a float')
    elif x <= 0.0:
        raise ValueError('x must be > 0.0')
    return (exp(x) / x)