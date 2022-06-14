"""
try-except

try:
    --------
    --------------
    --------- error
    ------------- will not be executed
    ------ will not be executed
except:
    --------------
    -------------

try:
    - Python tries to run the code
    - If no errors, it will finalize the try-except block
    - If there is an error, the execution will jump into the except block
except:
    - where you catch the exception
    - you do the necessary operations

"""

# Ex:
# the case with no exception handling
#
#
# def get_squares():
#     user_input = input('Enter a number: ')
#     num = int(user_input)
#     print(num**2)
#
#
# get_squares()
#


# # the case with exception handling


# def get_squares_try():
#
#     try:
#         user_input = input('Enter a number: ')
#         num = int(user_input)
#         print(num**2)
#     except:
#         print('Not a number....')
#
#
# get_squares_try()


# def get_squares_try_recursion():
#
#     try:
#         user_input = input('Enter a number: ')
#         num = int(user_input)
#         print(num**2)
#     except:
#         print('Not a number....')
#         get_squares_try_recursion()
#
#
# get_squares_try_recursion()


# Ex:
# Open a file

# Open a file that doesn't exist
# def open_file(path):
#     try:
#         # Open()
#         file = open(path)
#
#         # Loop over file line by line
#         for line in file:
#             print(line.split())
#
#     except:
#         # FileNotFoundError: No such file or directory
#         print(f'File not found in the specified location: {path}')
#
#
# path = 'seriees.txt'
# open_file(path)

"""
Handle more than one except blocks:
 - Multiple exceptions

except ExceptionType 1:

except ExceptionType 2:
"""

# Ex:
# Divide by Zero

def divide_number():

    try:
        # ValueError
        number_to_divide = int(input('Please enter a number to divide: '))
        divisor = int(input('Please enter the divisor: '))

        result = number_to_divide/divisor
        print(result)

    except ValueError:
        print('One or more than one input values are not numeric')
        print('Please enter the numeric values')

    except ZeroDivisionError:
        print('Second number cannot be zero')


divide_number()
