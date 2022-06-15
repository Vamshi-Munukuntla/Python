"""
Packages:
* Organize the Code
* Portable
* Arrange Modules
"""

"""
Python Packages -> are actually folders
* difference -> they include "__init__.py" file.
"""
#
# # Access a module under a Package
#
# import pack.mod_1 as m1, pack.mod_2 as m2
#
# print(m1)
# print(m2)

"""
__init__.py:

* in the __init__.py file:
    * sub packages and imports for modules
    * global variables
    * documentation
"""
#
# import pack
#
# print(pack.mod_1)

# When you import pack all the contents from "init" file gets imported into this file
'''
"""
This package has two modules:

* mod_1
* mod_2
"""

# wrong way

import mod_1
import mod_2

'''

from pack import mod_1

print(mod_1)