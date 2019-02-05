# C.1.1. : 9 - 3 --> 6
# C.1.2. : 8 * 2.5 --> 20.0
# C.1.3. : 9 / 2 --> 4
# C.1.4. : 9 / -2 --> -5
# C.1.5. : 9 % 2 --> 1
# C.1.6. : 9 % -2 --> -1
# C.1.7. : -9 % 2 --> 1
# C.1.8. : 9 / 2.0 --> 4.5
# C.1.9. : 4 + 3 * 5 --> 19
# C.1.10. : (4 + 3) * 5 --> 35

# C.2.1. : x = 100 --> x = 100
# C.2.2. : x = x + 10 --> x = 110
# C.2.3. : x += 20 --> x = 130
# C.2.4. : x = x - 40 --> x = 90
# C.2.5. : x -= 50 --> x = 40
# C.2.6. : x *= 3 --> x = 120
# C.2.7. : x /= 5 --> x = 24
# C.2.8. : x %= 3 --> x = 0

# C.3. : x = 3, x += x - x --> 1st Python will evaluate the right side of the
#  statement (x - x) with the value x = 3, so it will evaluate to 0. 2nd Python 
#  will add the value on the right side (0) to the current value of x (3) and 
#  set that equal to x. In the end, the value of x = 3. 

# C.4.1.1. : 1j + 2.4j --> 3.4j
# C.4.1.2. : 4j * 4j --> (-16+0j)
# C.4.1.3. : (1+2j) / (3+4j) --> (0.44+0.08j)
# C.4.2.1. : (1+2j) * (1+2j) --> (-3+4j)
# C.4.2.2. : 1+2j * 1+2j --> (1+4j)
# C.4.3. : They are different because Python will interpret the 2nd one as
#  1 + (2j * 1) + 2j due to order of operations. Thus giving an output of (1+4j).
#  From this we know that Python handles complex numbers as having 2 seperate 
#  parts, the real part and the imaginary part, that can be split up and are 
#  treated seperately when not in parentheses together.

# C.5.1. : cmath.sin(-1.0+2.0j) --> (-3.165778513216168+1.959601041421606j)
# C.5.2. : cmath.log(-1.0+3.4j) --> (1.2652585805200263+1.856847768512215j)
# C.5.3. : cmath.exp(-cmath.pi * 1.0j) --> (-1-1.2246467991473532e-16j)
# C.5.4. : It is better to write 'import math' and 'import cmath' because when
#  you do it this way you are able to call identically named methods from both.
#  For example, you can call both 'math.sqrt(4)' and 'cmath.sqrt(-4)' in two
#  consecutive lines without any additional code. However, if you
#  'from math imprt *' then 'from cmath import *', then you can no longer use
#  the 'math.sqrt()' method without going back to a 'from math import *'.

# C.6.1. : 'foobar'
# C.6.2. : 'foobar'
# C.6.3. : 'foobar'
# C.6.4. : Traceback (most recent call last):
#            Python Shell, prompt 15, line 1
#          invalid syntax: <string>, line 1, pos 3

# C.7. : 'A\nB\nC'

# C.8. : 80 * '-'

# C.9. : 'first line\nsecond line\nthird line'

# C.10. : 
x = 3
y = 12.5
'The rabbit is %d.' %x
'The rabbit is %d years old.' %x 
'%g is average.' %y
'%g * %d' %(y, x)
'%g * %d is %g.' %(y, x, y * x)

# C.11. : 
num = float(raw_input('Enter a number: '))
print num

# C.12. : 
def quadratic(a, b, c, x):
    return a * x ** 2 + b * x + c

# C.13. : 
def GC_content(x):
    '''Takes an input of a string of a combination of G, C, T, and A, 
    representing a DNA sequence, and returns a single float,
    which represents the proportion of the bases which are either G or C.
    '''
    a = float(x.count('G'))
    b = float(x.count('C'))
    return (a + b) / len(x)

