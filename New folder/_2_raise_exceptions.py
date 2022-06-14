# Collapse all code -> Ctrl + Shift + '-'

"""
No matter how hard you try to make your code free of bugs,
unfortunately at some point there might be errors.
To prevent your program to crash you have to handle these errors properly.

What you will do in this case?
You have to raise appropriate exceptions and decide what to do with these exceptions.

Appropriate Exception will help you to debug your code more easily.
Moreover, it will let other programs, who call your code, to understand what happened.

To raise an exception in Python -> raise
"""

"""
---------Raise---------
"""

"""
Ex:
We have asked for an integer many times from the user.
Let's do the same again.
But this time, if the user doesn't enter an integer we will raise an Exception.
"""


# def raise_exception():
#
#     user_input = input('please enter an integer: ')
#
#     # if we don't handle the error -> crash
#     # ValueError: invalid literal for int() with base 10: 'vasdfas'
#
#     if not user_input.isdigit():
#         raise Exception('Not a integer value...')
#     num = int(user_input)
#     print(num)
#
#
# raise_exception()

"""
Now that we know, we will get ValueError when the user does not enter an integer,
Let's refactor our code and raise ValueError instead of generic Exception.
"""

#
# def raise_defined_exception():
#
#     user_input = input('please enter an integer: ')
#
#     if not user_input.isdigit():
#         raise ValueError('Not a integer value...')
#     num = int(user_input)
#     print(num)
#
#
# raise_defined_exception()


"""
-----------   Assert   -----------
"""

"""
The if statement above was actually an 'assertion' operation.
That means, if the code has not been asserted, it will not move on.
Assertion makes sure the code to stop if it doesn't assert to True.

So for checking assertions instead of using 'if' statement we can use 'assert' statement.

assert <condition_to_check>

If 'continue_to_check' is not return True, then Python will raise an error.

We mainly use assertion statement for debugging purposes.
"""

"""
Let's write the same code above with assert statement.
"""


# def assert_user_input():
#
#     user_input = input('Enter an integer value: ')
#
#     assert int(user_input), ValueError('Not Asserted as integer...')
#
#     num = int(user_input)
#     print(num)
#
#
# assert_user_input()


def division(n1, n2):

    # assert the divisor not being zero
    # AssertionError -> exception
    assert n2 != 0, "You can't divide by zero."

    print(n1/n2)


division(10, 5)
division(1, 0)















