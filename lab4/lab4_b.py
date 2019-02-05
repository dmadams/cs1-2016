# B.1. 
import random
def random_size(low_bound, up_bound):
    '''Takes two arguments (both non-negative even integers, where the first 
    argument must be smaller than the second), and returns a random even 
    integer which is >= the lower number and <= the upper number.
    '''
    assert low_bound >= 0
    assert up_bound >= 0
    assert low_bound % 2 == 0
    assert up_bound % 2 == 0
    assert low_bound < up_bound
    out = random.randint(low_bound / 2, up_bound / 2)
    out *= 2
    assert out % 2 == 0
    return out

# B.2. 
def random_position(max_x, max_y):
    '''Takes as its arguments two integers called max_x and max_y, both of 
    which are >= 0. It will return a random (x, y) pair, with both x >= 0 and 
    y >= 0 and with x <= max_x and y <= max_y.
    '''
    assert max_x >= 0
    assert max_y >= 0
    x = random.randint(0, max_x)
    y = random.randint(0, max_y)
    return (x, y)

# B.3.
def random_color():
    '''Generates random color values in the format of #RRGGBB.
    '''
    hex_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b',\
                'c', 'd', 'e', 'f']
    color = '#'
    for a in range(6):
        color += random.choice(hex_list)
    return color

# B.4. 
def count_values(dic):
    '''Takes a single dictionary as an argument and returns a count of the 
    number of distinct values it contains.
    '''
    val = dic.values()
    c = 0
    diff_val = []
    for a in val:
        if a not in diff_val:
            c += 1
            diff_val.append(a)
    return c

# B.5. 
def remove_value(dic, item):
    '''Takes a dictionary and an arbitrary item which could be a value in the
    dictionary. It removes all key/value pairs from the dictionary which have 
    that value. If the value is not in the dictionary it does nothing. 
    It returns nothing.
    '''
    key = dic.keys()
    for a in key:
        if dic[a] == item:
            del dic[a]

# B.6.
def split_dict(dic):
    '''Takes as its argument a dictionary which uses strings as keys and 
    returns a tuple of two dictionaries whose key/value pairs are from the 
    original dictionary: those whose keys start with the letters a-m 
    (lower- or uppercase) and those whose keys start with the letters n-z 
    (lower- or uppercase). The original dictionary is not altered.
    '''
    dic_1 = {}
    dic_2 = {}
    for key in dic:
        if key[0] > 'n' or key[0].upper() > 'N':
            dic_2.update({key : dic[key]})
        else:
            dic_1.update({key : dic[key]})
    return (dic_1, dic_2)
        
#B.7.
def count_duplicates(dic):
    '''Takes a dictionary as an argument and returns the number of values that 
    appear two or more times.
    '''
    if len(dic) == 0:
        return 0
    lst = dic.values()
    c = 0
    while True:
        val1 = lst[0]
        lst.remove(val1)
        for val2 in lst:
            if val2 == val1:
                lst.remove(val2)
                c += 1
        if len(lst) == 0:
            break
    return c