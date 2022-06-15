"""
import <module_name>

Python looks for modules as follows:
1 - Searches the current folder that the code runs (same level)
2 - PYTHONPATH environment variable -> if it's defined system level
3 - In the folders where Python is installed (virtual environments)

sys.path -> displays Python search paths
"""

# # Search Paths of Python
# import sys
#
# python_search_path = sys.path
#
# for path in python_search_path:
#     print(path)


# # Directory Access
# import modules.module_input_operations as mio
#
# user_input = mio.get_integer()
# print(user_input)

"""
It is not a good practice to get modules with folder path.
Folder names or path may change and bring unnecessary code issues.
"""

"""
Best Practice

Project Level Access:
Modules&Packages\venv\lib\site-packages
"""

import own_module
a = own_module.get_integer()
print(a)

"""
System Level Access (global access):
...\Python\Python39\lib
"""
