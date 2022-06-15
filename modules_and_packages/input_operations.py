""""
This module is for input operations.
"""

def get_input(type = 'text'):

    return input(f'Please enter a/an {type}: ')

def get_integer():

    while True:
        try:
            user_input = get_input(type='integer')
            num = int(user_input)
        except Exception as e:
            print(e)
            continue
        else:
            return num


def get_float():

    while True:
        try:
            user_input = get_input(type='float')
            flt = float(user_input)
        except Exception as e:
            print(e)
            continue
        else:
            return flt
