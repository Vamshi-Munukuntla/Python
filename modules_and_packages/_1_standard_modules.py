# Standard modules

"""
Modular Programming:
1 - Prevents code repetition
2 - Better Organization (web, db, api...)
3 - Easy Maintainence
"""

"""
Module: A Python file ending with .py
Package: Python special folders including one or more modules
"""

"""
import
"""

"""------------------------------------ """


# import math
#
# # pi number
# pi_num = math.pi
# print(f'Pi Values is: {pi_num}')
#
# # random package
# import random
# probability = random.random()
# print(probability)
#
# # random number
# rand_num = random.randint(0,87)
# print(rand_num)
#
# # random list
# a_list = [1,2,3,4,5,6,7,8,9]
# rand_item = random.choice(a_list)
# print(rand_item)
#
# # random sample
# rand_sample = random.sample(a_list,3)
# print(rand_sample)
#
# # Platform
#
# import platform
# print(platform)
#
# # platform type
# print('Platform type: ', platform.platform())
#
# # platform architecture
# print('Platform Architecture: ', platform.architecture())
#
# # Machine Data
# print('Machine Data: ', platform.machine())
#
# # OS Data
# print("OS:", platform.system())

"""
OS Module
"""
#
# import os
#
# # print('OS Module:', os)
#
# # Current Folder of our project
# print(os.getcwd())
#
# # Logged in user
# print(os.getlogin())

"""
sys
"""

# import sys
#
# # Path Variable
# paths = sys.path
#
# print("Python search paths for modules: ")
# for path in paths:
#     print(path)
#
# # sys.path -> the list where Python looks for modules.

"""
import syntax
* import ......... as ...

Multiple imports
* import math, sys, random

Import Specific Packages
* from ...... import ....

Import Specific Packages and aliasing/ renaming
* from ....... import ..... as ...

Import all (not advisable)
* from ... import *
"""

# import random as rnd
#
# print(rnd.randint(2, 10))

# import math, random, sys
#
# # sub module
#
# from sys import modules
# for i in modules:
#     print(i)

# from math import sqrt
# print(sqrt(16))

# Aliasing Sub Module
from math import sqrt as sq
print(sq(25))


















