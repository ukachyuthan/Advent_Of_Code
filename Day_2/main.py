'''

Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?

Input is input file

'''

import numpy as np
import re
from collections import Counter

def password_check(name):
    h = open(name, 'r')
    content = h.readlines()
    password = []
    min_ = []
    max_ = []
    targ = []
    for line in content:
        password.append(line.split(':')[1][:-1])
        line = line.split()
        line[0] = line[0].split('-')
        min_.append(int(line[0][0]))
        max_.append(int(line[0][1]))
        targ.append(line[1][:-1])
    valid = 0
    #check for Problem 1
    for i in range (1000):
        sum = 0
        c = Counter(password[i])
        if c[targ[i]] >= min_[i] and c[targ[i]] <= max_[i]:
            valid = valid+1
    print(valid)
    #check for problem 2
    valid_ = 0
    for i in range(999):
        print(i)
        if (targ[i] == password[i][min_[i]] and targ[i] != password[i][max_[i]]) or (targ[i] != password[i][min_[i]] and targ[i] == password[i][max_[i]]):
            valid_ += 1
    print(valid_)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    password_check('input.txt')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
