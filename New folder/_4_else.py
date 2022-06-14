"""
try:
    ...
    ........
    .....
except Ex1:
    ......
    ..........
except Ex2:
    .............
    ..........
    .................
    ....
else:
    ......
    ..........
    .........

Python Interpreter runs the code in try block
If there is an error, the execution goes into the related except block.
If there is no error, then it will move on to else block.
"""

# Ex:


# def open_file(path):
#
#     try:
#         file = open(path,encoding='utf-8')
#     except FileNotFoundError:
#         print('No file path:', path)
#     else:
#         print(file.read())
#
#
# open_file('series.txt')


"""
Get the standard error text:
    
    except ExceptionType as <name>:

"""


# def open_file_as_exc(path):
#
#     try:
#         file = open(path)
#     except FileNotFoundError as e:
#         print(e)
#     else:
#         print(file.read())
#
#
# open_file_as_exc('series.txt')

























