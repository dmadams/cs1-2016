# Name: David Adams
# CMS Login: dmadams

# 1.1.

# Error 1: In line 4, there should be 3 (')s not 2 (")s.
# Error 2: In line 6, there should be 3 (')s not 2 (")s.
# Error 3: In line 7, there is no n in the second half of the or statement.
# Error 4: In line 9, there should be 2 equal signs.
# Error 5: In line 11, there should be a colon after else. 

# from math import sqrt
# 
# def is_prime(n):
#     ""                               1. (''')
#     Return True if 'n' is prime; else return False.
#     ""                               2. (''')
#      if n == 2 or == 3:              3. (if n == 2 or n == 3:)
#          return True
#      elif n % 2 = 0:                 4. (elif n % 2 == 0:)
#          return False
#      else                            5. (else:)
#          for i in range(5, int(sqrt(n) + 1), 2):  # odd #s >= 5
#              if n % i == 0:
#                  return False
#          return True


# 1.2. 

# Error 1: result is referenced in line 11 before it is given a value.
# Error 2: In line 10, it should be break not return.
# Error 3: Since 1 is subtracted from n in line 8, only multiplying by n in 
# line 11 will not give the correct answer. Instead result should be multiplied 
# by n + 1. 
# Error 4: For the function to return result it must be return result not print
# result in line 12. 
# Error 5: In line 24, when adding i / factorial(i) to result, 
# both i and factorial of i are int type, but for i > 2 factorial(i) > i, so it
# will return 0. At least one of these numbers must be converted to a float. 

# def factorial(n):
#     '''
#     Compute and return the factorial of n i.e.
#     n * (n - 1) * (n - 2) * ... * 1, or 1 if n == 0.
#     '''
#     assert n >= 0
#                                      1. (result = 1)
#     while True:
#         n -= 1
#         if n <= 0:
#             return                   2. (break)
#         result = n * result          3. (result *= n + 1)
#     print result                     4. (return result)

# def e(limit):
#     '''
#     Estimate the constant e (2.71828...) by the series expansion:

#       e = sum (i from 0 to infinity) (i / factorial(i)),

#     except we use a limit to cut off the expansion
#     (OK if the limit is large enough).
#     '''
#     result = 0
#     for i in range(0, limit + 1):  # 0 to limit, inclusive
#         result += i / factorial(i)   5. (result += i / (float(factorial(i))))
#     return result

# print e(20)  # should print 2.7182818284590455


# 1.3. 

# Error 1: The name of the function w is not descriptive. 
# Error 2: The names of the variables x, y, and z are not descriptive. 
# Error 3: The docstring should have triple quotes.
# Error 4: The docstring does not make any sense and is nearly unreadable with
# how abbreviated and nondescriptive it is. 
# Error 4: In line 3, there should be spaces before and after the equal sign.
# Error 5: In line 5, there should be spaces before and after all the
# mathematical operators (>=, -, <=, and +).
# Error 6: The indents for the if and else statements in lines 5 and 7 are 
# wrong.
# Error 7: The indent in line 8 is wrong.
# Error 8: There should be spaces before and after the += sign.
# Error 9: In line 8, there should be spaces before and after the equal sign.

# def w(x, y, z): 
#     "rt es in x in [y-z,y+z]."
#     v=[]
#     for i in x:
#      if i>=y-z and i<=y+z:
#                v+=[i]
#      else:
#          i=i
#     return v


# 2.1.
def draw_box(n):
    '''Takes a positive integer n as an argument and returns a string which, 
    when printed, will draw a box made up of '+' characters (the corners), 
    '-' characters (the top and bottom edges), '|' characters (the left and 
    right edges) and the interior of the box will be made up of blank 
    characters (' '), (lower-case) 'x' characters, and (lower-case) 'o'
    characters in a right-triangular pattern alternating 'x' and 'o' characters.
    The size of the interior of the box will be n by n characters. The box, 
    when printed, will also have a leading and trailing blank line.
    '''
    assert n > 0
    strng = '\n+'
    strng += n * '-' + '+\n'
    for i in range(n):
        strng += '|'
        for j in range(i + 1):
            if (i + 1) % 2 != 0:
                if (j + 1) % 2 != 0:
                    strng += 'x'
                else:
                    strng += 'o'
            else:
                if (j + 1) % 2 != 0:
                    strng += 'o'
                else:
                    strng += 'x'
        strng += (n - (i + 1)) * ' ' + '|\n' 
    strng += '+' + n * '-' + '+\n'
    return strng


# 2.2.1.
import random
def hypervolume(d, nmax):
    '''Takes 2 arguments: d- the number of dimensions of the hypersphere (must 
    be an integer >= 2) and nmax- the number of randomly generated points. The 
    function will generate nmax points, each of which will have d random 
    coordinates. It then counts the number of points that lie inside hypersphere
    of radius 1. It divides this count by nmax and multiplies by 2 ** d to 
    obtain an estimate for the hypervolume of the shape, which is returned. 
    '''
    c = 0
    for i in range(nmax):
        point = []
        for j in range(d):
            point.append(random.random())
        distance_squared = 0
        for k in range(len(point)):
            distance_squared += point[k] ** 2
        if distance_squared <= 1:
            c += 1
    return (float(c) / float(nmax)) * 2 ** d


# 2.2.2.
from math import *
def correct_hypervolume(d):
    '''
    Compute the hypervolume of a hypersphere of dimension 'd' and radius = 1.

    Argument: d (number of dimensions (>= 2))
    Return value: the hypervolume
    '''
    assert d >= 2
    if d == 2:
        return pi
    elif d == 3:
        return 4.0 / 3.0 * pi
    else:
        return (2.0 * pi / d) * correct_hypervolume(d - 2)

def print_hypervolumes(dmax, nmax):
    '''Takes 2 arguments: dmax- the maximum number of dimensions considered and
    nmax- the number of randomly generated points. For each dimension d where
    2 <= d <= dmax, the function will print a statement of the format below with
    the number of dimensions, the estimated hypervolume, the correct
    hypervolume, and the percent error.
    
    >>> print_hypervolumes(4, 10000)
    iterations: 10000
    
    dimension: 2
    estimated hypervolume: 3.152800
    correct hypervolume: 3.141593
    error: 0.356741 %
    
    dimension: 3
    estimated hypervolume: 4.119200
    correct hypervolume: 4.188790
    error: 1.661344 %
    
    dimension: 4
    estimated hypervolume: 4.880000
    correct hypervolume: 4.934802
    error: 1.110525 %
    
    '''
    print 'iterations: %d\n' % nmax
    for d in range (2, dmax + 1):
        estimate = hypervolume(d, nmax)
        correct = correct_hypervolume(d)
        error = abs((estimate - correct) / correct) * 100
        print 'dimension: %s' %d
        print 'estimated hypervolume: %f' %estimate
        print 'correct hypervolume: %f' %correct
        print 'error: %f %%\n' %error


# 2.3.
def encode(strng):
    '''Takes as an argument a string to be encoded. Returns a string with all
    vowels replaced according to the table below:
    a --> at
    e --> eat
    i --> iota
    o --> outer
    u --> uniter
    '''
    code_dic = {'a' : 'at', 'e' : 'eat', 'i' : 'iota', 'o' : 'outer', \
                    'u' : 'uniter'}
    new_strng = ''
    for char in strng:
        if code_dic.has_key(char):
            new_strng += code_dic[char]
        else:
            new_strng += char
    return new_strng  

def decode(strng):
    '''Takes as an argument a string encoded by the encode method. Returns the
    decoded version of the string. 
    '''
    decode_dic = {'at' : 'a', 'eat' : 'e', 'iota': 'i', 'outer' : 'o', \
                  'uniter' : 'u'}
    new_strng = ''
    key_lst = decode_dic.keys()
    while len(strng) > 0:
        for i in range(len(strng)/2):
            for key in key_lst:
                if strng.startswith(key):
                    new_strng += decode_dic[key]
                    strng = strng[len(key):]
        new_strng += strng[0:1]
        strng = strng[1:]        
    return new_strng


# 3.1.
def logistic_iter(r, x, niters, nsave):
    '''Takes 4 arguments:
    r(a float): the r parameter of the logistic function
    x(a float): the starting x value of the logistic function
    niters(an int): the number of iterations of the logistic function to compute
    nsave(an int): the number of iterates to return
    
    This function takes the initial x and r values and computes the output of 
    the logistic function on those values. It then uses that output as the new 
    input x value to compute yet another output, then uses that output as the 
    new input x value again, and so on. The r value stays the same throughout. 
    The function continues until niters iterates have been computed, and saves 
    the last nsave iterates, returning them as a list in the order they were 
    generated.
    '''
    assert r > 0.0
    assert 0.0 < x and 1.0 > x
    assert nsave >= 0 and nsave <= niters
    save_lst = []
    while niters > 0:
        current_val = r * x * (1 - x)
        if nsave >= niters:
            save_lst.append(current_val)
        x = current_val
        niters -= 1
    assert len(save_lst) == nsave
    return save_lst

def logistic_print(r, x, niters, nsave, split):
    '''
    Print out the iterates of an iterated logistic function test run
    to the terminal in such a way to make it easy to detect limit cycles.

    Arguments:
      r      -- logistic equation parameter
      x      -- starting x value (between 0.0 and 1.0)
      niters -- number of iterations of the logistic function
      nsave  -- number of iterates to return
      split  -- number of iterates printed before printing a blank line
    
    Return value: none
    '''

    assert split > 0

    s = logistic_iter(r, x, niters, nsave)
    print 'r = %.6f\tx = %.2f\tniters = %d\tnsave = %d\n' % \
            (r, x, niters, nsave)
    count = 1
    for item in s:
        print "%.6f" % item
        if count % split == 0 and split != 1:
            print
        count += 1
    print
    raw_input('press any key... ')


# 3.2.
def logistic_time_series(rs, x, niters, nsave, filename, yrange):
    '''Takes 6 arguments:
    rs(a list): a list of r values for the logistic function
    x(a float): the starting x value of the logistic function
    niters(an int): the number of iterations of the logistic function to compute
    nsave(an int): the number of iterates to return
    filename(a string): the name of the file to save to
    yrange(a string): either 'auto' (for automatic y range), or 'full' (for y 
    range from 0 to 1)
    
    This function generates two output files. The first will have the same name
    as the filename argument and will be the raw output of the runs of 
    logistic_iter as described below. The second will be the instructions to 
    the gnuplot program to plot the data in the first file.
    
    For each r value in the list rs, it calls the logistic_iter function with 
    the appropriate arguments and saves the results. It writes this data to the
    output file, with one line for each point at a given location in each of 
    the result lists, as well as a number representing which point it is.
    
    Example: 
    logistic_time_series([0.4, 1.9, 2.5], 0.3, 50, 50, 'time_series', 'auto')
    0 0.084 0.399 0.525 
    1 0.0307776 0.455618 0.623437 
    2 0.0119321 0.471257 0.586908 
    3 0.0047159 0.47343 0.606118
    ...
    49 2.31693e-21 0.473684 0.6
    '''
    f = open(filename, 'w')
    results = []
    for r in rs:
        results.append(logistic_iter(r, x, niters, nsave))
    for i in range(nsave):
        f.write('%d' %i)
        for j in range(len(rs)):
            lst = results[j]
            f.write(' %f' %lst[i])
        f.write('\n')
    f.close()
    
    file = open(filename + '.gp', 'w')
    if yrange != 'auto':
        print >> file, 'set yrange [0:1]'
    for (i, r) in enumerate(rs):
        print >> file, 'set title "r = %g" font ",24"' % r
        print >> file, 'set nokey'
        print >> file, "set style line 1 lc rgb 'blue' pt 6 ps 1.5"
        print >> file, 'plot "%s" using 1:%d with linespoints ls 1' % \
            (filename, i+2)
        print >> file, 'pause -1 "hit any key to continue..."'
        print >> file
    file.close()


# 3.3.
from math import *
def find_period(r, x, niters, nsave, precision):
    '''Takes 5 arguments:
    r(a float): the r parameter of the logistic function
    x(a float): the starting x value of the logistic function
    niters(an int): the number of iterations of the logistic function to compute
    nsave(an int): the number of iterates to return
    precision(a float): the smallest increment to consider two floating-point 
    numbers different
    
    This function computes the period of a limit cycle of the iterated logistic
    function for a particular r parameter value and a particular starting point 
    x.
    '''
    lst = logistic_iter(r, x, niters, nsave)
    c = 0
    while True:
        new_lst = []
        num_1 = lst[0]
        lst.remove(num_1)
        for num_2 in lst:
            if abs(num_1 - num_2) > precision:
                new_lst.append(num_2)
        lst = new_lst
        c += 1
        if len(lst) == 0:
            break
    if c == nsave:
        c = -1
    return c    


# 3.4. 
def is_power_of_two(n):
    return n in [1,2,4,8,16,32,64,128,256,512,1024,2048,4096]

def find_bifurcation_point(x, niters, nsave, prec1, prec2, period):
    '''Takes 6 arguments:
    r(a float): the r parameter of the logistic function
    x(a float): the starting x value of the logistic function
    niters(an int): the number of iterations of the logistic function to compute
    nsave(an int): the number of iterates to return
    prec1(a float): the precision argument for find_period
    prec2(a float): the precision of the estimate of the bifurcation point
    period(an int): the period to look for (must be a power of 2)
    
    This function returns the value of the r parameter at which the bifurcation
    to that period occurs (within the precision prec2).
    '''
    low = 0.0
    hi = 4.0
    while True:
        mid = low + ((hi - low) / 2)
        prd = find_period(mid, x, niters, nsave, prec1)
        if is_power_of_two(prd) and prd <= period / 2:
            low = mid
        else:
            hi = mid
        if hi - low < prec2:
            return mid


# 3.5. 
from math import *
def find_feigenbaum_constant(x, niters, nsave, prec1, prec2, period):
    '''Takes 6 arguments:
    x(a float): the starting x value of the logistic function
    niters(an int): the number of iterations of the logistic function to compute
    nsave(an int): the number of iterates to return
    prec1(a float): the precision argument for find_period
    prec2(a float): the precision of the estimate of the bifurcation point
    period(an int): the maximum period to look for (must be a power of 2)
    
    This function does not return anything, but will print out successive 
    estimates of Feigenbaum's constant along with the maximum period. It will 
    do this by calling find_bifurcation_point for periods of successive powers
    of 2 up to the maximum period. The estimates should converge to Feigenbaum's
    constant (which is 4.669201609...).
    
    Example:
    find_feigenbaum_constant(0.3, 1000000, 2048, 1.0e-6, 1.0e-10, 128)
    8 4.75141
    16 4.65618
    32 4.66812
    64 4.66852
    128 4.66875
    '''
    for i in range(1, int(log(period, 2) - 1)):
        b1 = find_bifurcation_point(x, niters, nsave, prec1, prec2, 2 ** i)
        b2 = find_bifurcation_point(x, niters, nsave, prec1, prec2, 2 ** (i+1))
        b3 = find_bifurcation_point(x, niters, nsave, prec1, prec2, 2 ** (i+2))
        estimate = (b2 - b1) / (b3 - b2)
        print '%d %f' %(2 ** (i + 2) , estimate)
    