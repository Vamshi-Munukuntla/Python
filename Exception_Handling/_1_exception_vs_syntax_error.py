"""
1 - Exception vs. Syntax Error:

A Python program stops execution when it encounters an error.
The process of managing these situations is called Exception Handling.

There are two types of errors in Python:
 * Syntax Error (Design-Time error)
 * Exception (Run-Time error)
"""

""" 
Syntax Error (Design-Time Error):
If the code you write doesn't comply with Python Syntax, the Python Parser will raise "Syntax Error".

Error Type: SyntaxError
"""

# Ex:
# SyntaxError: unmatched ')'
# print('No Syntax Error') # No Error Occurs
# print('Python Parser Error')) # Syntax Error Occurs


# Ex:
# SyntaxError: unterminated string literal
# a = "12'
# print(a)


# Ex:
# IndentationError: expected an indented block after function definition
# def myfunc():
# print('12')

"""
Exception:
Let's say, your code is syntactically correct.
So it will start execution.
If it causes an error during the execution (run-time). 
Python Interpreter will raise an error.
This type of of error is called Exception in general
"""

# Ex:
# ZeroDivisionError: division by zero
# print(9/0)


# Ex:
# NameError: name 't' is not defined
# print(t)


# Ex:
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# a = 12
# b = 'B'
# print(a+b)

