# B.1.
from math import *
class Point:
    '''Represents a point in 3D Euclidean coordinates (real values).
    '''
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distanceTo(self, point2):
        '''Calculates and returns the distance between 2 Points. 
        '''
        dist = sqrt((self.x - point2.x)**2 + (self.y - point2.y)**2 + \
                    (self.z - point2.z)**2)
        return dist

# B.2.
class Triangle:
    '''Represents a triangle using 3 Points. 
    '''
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def area(self):
        '''Computes and returns the area of a Triangle.
        '''
        a = self.p1.distanceTo(self.p2)
        b = self.p2.distanceTo(self.p3)
        c = self.p3.distanceTo(self.p1)
        s = (a + b + c) / 2
        area = sqrt(s * (s - a) * (s - b) * (s - c))
        return area

# B.3. 
class Averager:
    '''Stores a list of numbers nums, the total of the numbers within the list 
    total, and the length of the list n. Performs various operations on the list
    of numbers.
    '''
    def __init__(self):
        self.nums = []
        self.total = 0
        self.n = 0

    def getNums(self):
        '''Returns a copy of nums. 
        '''
        lst = []
        for i in self.nums:
            lst.append(i)
        return lst

    def append(self, num):
        '''Appends a number num to the end of the list nums.
        '''
        self.nums.append(num)
        self.n += 1
        self.total += num

    def extend(self, lst):
        '''Extends the list nums by another list of numbers lst.
        '''
        self.nums.extend(lst)
        self.n += len(lst)
        for i in lst:
            self.total += i

    def average(self):
        '''Calculates and returns the average of nums. If nums is empty, returns
        0.
        '''
        if self.n == 0:
            return 0
        avg = float(self.total) / float(self.n)
        return avg

    def limits(self):
        '''Finds and returns the minimum and maximum values within nums as a 
        tuple. If nums is empty, returns (0, 0).
        '''
        if self.n == 0:
            return (0, 0)
        min = self.nums[0]
        max = self.nums[0]
        for i in self.nums:
            if i < min:
                min = i
            if i > max:
                max = i
        return (min, max)

# C.1.1. 
# The if and else statements are unnecessary since x > 0 evaluates to either
# True or False so you can just return that.
def is_positive(x):
    '''Test if x is positive.'''
    return x > 0

# C.1.2.
# The code is overally complex and has unnecessary if and else statements and 
# variables, such as found and location.
def find(x, lst):
    '''Returns the index into a list where x is found, or -1 otherwise.
    Assume that x is found at most once in the list.'''
    for i in range(len(lst)):
        if lst[i] == x:
            return i
    return -1

# C.1.3.
# The code runs unnecessary checks after already determining the category. For
# example, if x < 0 then there is no reason for the code to continue checking
# if x == 0 and so on. Also, there is no need to check for 'large' since if x
# is not in any of the other categories it must be in 'large'.
def categorize(x):
    '''Return a string categorizing the number 'x', which should be
    an integer.'''
    if x < 0:
        return 'negative'
    elif x == 0:
        return 'zero'
    elif x > 0 and x < 10:
        return 'small'
    return 'large'

# C.1.4.
# The if and elif statements are completely unnecessary. Also, there is no
# reason to include the total variable. 
def sum_list(lst):
    '''Returns the sum of the elements of a list of numbers.'''
    answer = 0
    for item in lst:
        answer += item
    return answer
