# B.1. :
def complement(dna):
    '''Takes an input of a string composed of only the letters 'A', 'C', 'G', 
    and 'T' (representing DNA) and returns an output of the 
    complement.
    '''
    dna2 = ''
    for a in dna:
        if a == 'A':
            dna2 += 'T'
        elif a == 'T':
            dna2 += 'A'
        elif a == 'C':
            dna2 += 'G'
        else:
            dna2 += 'C'
    return dna2

# B.2. :
def list_complement(dna):
    '''Takes an input of a list of the letters 'A', 'C', 'G', and 'T' 
    (representing DNA) and changes the list to its complement. This method
    does not return anything.
    '''
    for a in range(len(dna)):
        if dna[a] == 'A':
            dna[a] = 'T'
        elif dna[a] == 'T':
            dna[a] = 'A'
        elif dna[a] == 'C':
            dna[a] = 'G'
        else:
            dna[a] = 'C'

# B.3. :
def product(nums):
    '''Takes an input of a list of numbers and computes the product of the 
    entire list and returns it. If the list is empty, it returns 1.
    '''
    x = 1
    for a in nums:
        x *= a
    return x

# B.4. : 
def factorial(x):
    '''Takes an input of a non-negative integer and returns the factorial of
    that integer.
    '''
    if (x == 0):
        return 1
    else:
        nums = range(1, x + 1)
        return product(nums)
# B.5. :
import random
def dice(m, n):
    '''Takes two inputs m (the number of sides one die has) and n (the number
    of dice) and simulates the rolling of those dice. Returns the sum of the
    dice rolls. 
    '''
    d = range(1, m + 1)
    x = 0
    for a in range(n):
        x += random.choice(d)
    return x

# B.6. :
def remove_all(nums, x):
    '''Takes two inputs nums (a list of integers) and x (an integer) and 
    removes every occurrence of x from nums. Does not return anything. 
    '''
    while nums.count(x) > 0:
        nums.remove(x)

# B.7. :
def remove_all2(nums, x):
    '''An improved version of remove_all using the count method.
    '''
    for a in range(nums.count(x)):
        nums.remove(x)

def remove_all3(nums, x):
    '''An improved version of remove_all using the in operator.
    '''
    while x in nums:
        nums.remove(x)

#B.8. :
def any_in(nums1, nums2):
    '''Takes two lists as inputs and returns True if any of the elements in
    the first list are in the second list. Otherwise, it returns False.
    '''
    for a in nums1:
        if a in nums2:
            return True
    return False

# C.1.a. : 
# Ignoring the typo, in the if statement there should be 2 equal signs not 1.
# It should read if a == 0.

# C.1.b. : 
# s is in quotes, so it will be interpreted as the literal string 's'. Remove
# the quotes to fix it.

# C.1.c. : 
# The 2nd s is now in quotes, so it will always return the string 's-Caltech'. 
# Remove the quotes to fix it.

# C.1.d. : 
# You cannot concatenate a list with a string, which is what Python will
# interpret this as. Instead you can add 'bam' as the last element of lst by
# using lst.append('bam').

# C.1.e. : 
# lst.reverse() changes lst. It cannot be assigned as a new list to lst2. 
# Instead you could say:
# lst.reverse()
# lst.append(0)
# return lst

# C.1.f. :
# First, it is using list and str as variable names, which is bad form and 
# can mess things up. Instead, you can use lst and s. Also, when you use append
# like it does here it will append a list into the list. i.e. 
# s = ['a', 'b']
# append_string_letters_to_list(s, 'cdef')
# s --> ['a', 'b', ['c', 'd', 'e', 'f']]
# To fix it:
# def append_string_letters_to_list(lst, s):
#     letters = list(s)
#     for a in letters:
#         lst.append(a)

# C.2. :
# Python will interpret the code in order, so in line 3 c will be set equal to 
# a + b (30) before a is changed to 30 in line 4. Thus the code will print 30.

# C.3. :
# add_and_double_2 does not return anything so it cannot be expected to output
# anything in another method. Print statements simply "print out" something,
# they do not "return" anything that can be used by another function.

# C.4. : 
# sum_of_squares_2 is not defined with any parameters, so it cannot have any
# parameters passed into it. When you ask the user for input using raw_input
# the function stops and asks the user to assign a variable to a certain 
# value. This will not work in the above sitaution though because you are
# attempting to use two specific parameters instead of whatever the user
# inputs.

# C.5. :
# In python you cannot assign a specific character in a string to a new
# character. Instead you could do:
# a = s[0].upper()
# b = s[1:]
# return a + b

# C.6. :
# When going through a for loop of this format, Python considers each item in
# lst individually. What this means is that if you change item, it will not 
# affect lst or any of the elements in lst. item is completely seperate from
# lst when you are trying to change it. 