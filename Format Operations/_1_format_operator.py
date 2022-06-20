"""
$ Operator

- %s -> string
- %d -> integer
- %f -> float
        - %.<n>f -> n decimal places
"""

import math

day = 'Sunday'
print('Today is %s' % day)

num = 19
print("Today's date is %d" % num)

pi = math.pi
print('The value of pi is % f'% pi)

# only 2 decimal places
print('The value of pi is %.2f' % pi)

# More than one %
print("Python language is released in %d, and it's been more than %d years" % (1991, 30))

# Dictionary with % operator
file = {
    'Path': './com/pty.py',
    'Version': 3.10,
    'Author': 'Vamshi Munukuntla'
}

file_info = 'The file path is %(Path)s, and the version is %(Version)s, and also the author is %(Author)s' % file
print(file_info)
