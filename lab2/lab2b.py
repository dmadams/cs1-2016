# D.1. : 
import random
def make_random_code():
    choices = ['R', 'G', 'B', 'Y', 'O', 'W']
    s = ''
    for a in range(4):
        s += random.choice(choices)
    return s
      
# D.2. :
def count_exact_matches(s1, s2):
    c = 0
    for a in range(4):
        if (s1[a] == s2[a]):
            c += 1
    return c

# D.3. :
def count_letter_matches(s1, s2):
    l1 = list(s1)
    l2 = list(s2)
    for a in range(4):
        if (l1[a] in l2):
            l2.remove(l1[a])
    return 4 - len(l2)

# D.4. :
def compare_codes(code, guess):
    b = count_exact_matches(code, guess)
    w = count_letter_matches(code, guess) - b
    e = 4 - (b + w)
    return b * 'b' + w * 'w' + e * '-'

# D.5. : 
def run_game():
    print 'New game.'
    code = make_random_code()
    n = 0
    x = ''
    while x != 'bbbb':
        guess = raw_input('Enter your guess: ')
        x = compare_codes(code, guess)
        print 'Result: %s' %x
        n += 1
    print 'Congratulations! You cracked the code in %d moves!' %n
    
    
    