# B.1. :
def list_reverse(lst1):
    ''' Takes as input a list and returns the reverse of the list without 
    changing the original list.
    '''
    lst2 = lst1[:]
    lst2.reverse()
    return lst2

# B.2. :
def list_reverse2(lst1):
    '''Takes as input a list and returns the reverse of the list without 
    changing the original list. Does not use the reverse function.
    '''
    lst2 = []
    for x in range(len(lst1) - 1, -1, -1):
        lst2.append(lst1[x])
    return lst2

# B.3. :
def file_info(fname):
    '''Takes a single input (a string representing the name of a text file), 
    and returns the number of lines, the number of words, and the number of 
    characters in the file as a tuple with three components 
    (line count, word count, character count).
    '''
    fle = open(fname, 'r')
    l_count = 0
    w_count = 0
    c_count = 0
    while True: 
        x = fle.readline()
        if x == '':
            break
        l_count += 1
        c_count += len(x)
        y = x.split()
        w_count += len(y)
    fle.close()
    return (l_count, w_count, c_count)
        
# B.4. : 
def file_info2(fname):
    '''Takes a single input (a string representing the name of a text file), 
    and returns the number of lines, the number of words, and the number of 
    characters in the file as a dictionary.
    '''    
    val = file_info(fname)
    dic = {'lines' : v[0], 'words' : v[1], 'characters' : v[2]}
    return dic

# B.5. :
def longest_line(fname):
    '''Takes as input the name of a text file and returns the length of the 
    longest line of the file, as well as the line itself as a (length, line) 
    tuple. If there are multiple lines of the same length, it returns the 
    first line. 
    '''
    fle = open(fname, 'r')
    c = 0
    lne = ''
    while True:
        x = fle.readline()
        if x == '':
            break
        if len(x) > c:
            c = len(x)
            lne = x
    fle.close()
    return (c, lne)

# B.6. :
def sort_words(str):
    '''Takes a string input, splits it into a list of words at spaces, and
    returns an alphabetically sorted list of the words. 
    '''
    lst = str.split()
    lst.sort()
    return lst

# B.7. :
# 11011010 = 0 * (2**0) + 1 * (2**1) + 0 * (2**2) + 1 * (2**3) 
#           + 1 * (2**4) + 0 * (2**5) + 1 * (2**6) + 1 * (2**7)
#          = 218
# The largest 8-digit binary number is 11111111 = 255

# B.8. :
def binaryToDecimal(bi_num):
    '''Takes a list of 0s and 1s (representing a binary number) as input and 
    convert it into an integer and returns it. 
    '''
    num = 0
    j = len(bi_num) - 1
    for x in bi_num:
        num += x * 2**j
        j -= 1
    return num

# B.9. : 
import math
def decimalToBinary(num):
    '''Takes an input of an integer and returns a list of 0s and 1s 
    (representing a binary number). 
    '''
    if num == 0:
        return [0]
    bi_num = []
    j = int(math.log(num, 2)) + 1
    while num > 0 and j > -1:
        if (num - 2**j) >= 0:
            bi_num.append(1)
            num -= 2**j
        elif (num - 2**j) < 0 and len(bi_num) >= 1:
            bi_num.append(0)
        if num == 0:
            break
        j -= 1
    while j > 0:
        bi_num.append(0)
        j -= 1
    return n

# C.2.1. :
# Style mistakes: Name of function is not descriptive, no spaces after commas, 
# no spaces before or after * and +
def sum_of_cubes(a, b, c):
    return a * a * a + b * b * b + c * c * c

# C.2.2. :
# Style mistakes: Name of function is hard to read, docstring is wrong, 
# argument names are hard to read, the return line is too long
def sum_of_cubes(arg_a, arg_b, arg_c, arg_d):
    '''returns the sum of the cubes of arg_a, arg_b, arg_c, and arg_d
    '''
    return arg_a**3 + arg_b**3 + arg_c**3 + arg_d**3

# C.2.3. :
# Style mistakes: There is no blank line between the two methods, the indents 
# are different
def sum_of_squares(x, y):
    return x * x + y * y

def sum_of_three_cubes(x, y, z):
    return x * x * x + y * y * y + z * z * z

