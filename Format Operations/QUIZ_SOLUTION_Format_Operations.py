"""
 [10 Questions] QUIZ - Format Operations
"""

#--------------------------------------------------------------------------------------#

# Q 1:
"""
Define a function named 'day_names'.
It will ask for a day name from the user.
And will return a Tuple including the day name and number of letters in it.
Ex: (Sunday, 6)

Call this function and get the result Tuple, and then print the string below:
'Sunday has 6 letters.'

Hints:
* use % operator
"""

# S 1:

def day_names():
    name = input('Please enter a day name: ')
    return (name, len(name))


# day, num_of_letters = day_names()
# print("%s has %d letters." % (day, num_of_letters))
# print("%s has %d letters." % day_names())


#--------------------------------------------------------------------------------------#

# Q 2:
"""
Call the function in Q1 and print the result with str.format() as follows:
'day: Monday, length: 6'
"""

# S 2:

# day, num_of_letters = day_names()
# print('day: {0}, lenght: {1}'.format(day, num_of_letters))


#--------------------------------------------------------------------------------------#

# Q 3:
"""
Call the function in Q1 and print the result with f-strings as follows:
'day: Monday, length: 6'
"""

# S 3:

# day, num_of_letters = day_names()
#
# print(f"day: { day }, length: {num_of_letters}")

#--------------------------------------------------------------------------------------#

# Q 4:
"""
Call the function in Q1 and print the result with Template Strings as follows:
'day: Monday, length: 6'
"""

# S 4:

from string import Template

# day, num_of_letters = day_names()
#
# template = Template('day: $x, length: $y')
# print(template.substitute(x=day, y=num_of_letters))


#--------------------------------------------------------------------------------------#

# Use the dictionary below for Questions 5, 6, 7, 8, 9, 10:
capitals = {
    'USA': 'Washington',
    'China': 'Beijing',
    'Germany': 'Berlin',
    'UK': 'London'
}

#--------------------------------------------------------------------------------------#

# Q 5:
"""
Use the capitals dictionary and % operator to print as follows:
"The capital city of USA is Washington"
'USA' will be constant, 'Washington' will be a variable.
"""

# S 5:

# s = "The capital city of USA is %(USA)s" % capitals
# print(s)


#--------------------------------------------------------------------------------------#

# Q 6:
"""
Use the capitals dictionary and str.format() to print as follows:
"The capital city of Germany is Berlin"
Both 'Germany' and 'Berlin' will be variables.
"""

# S 6:

country = 'Germany'
# s = "The capital city of {0} is {1}".format(country, capitals[country])
# print(s)


#--------------------------------------------------------------------------------------#

# Q 7:
"""
Use the capitals dictionary and f-strings to print as follows:
"The capital city of UK is London"
Both 'UK' and 'London' will be variables.
"""

# S 7:

country = 'UK'
# s = f"The capital city of {country} is {capitals[country]}"
# print(s)


#--------------------------------------------------------------------------------------#

# Q 8:
"""
Use the capitals dictionary and Template Strings to print as follows:
"The capital city of USA is Washington"
Both 'USA' and 'Washington' will be variables.
"""

# S 8:
from string import Template

# country = 'USA'
# template = Template('The capital city of $co is $ca')
# print(template.substitute(co=country, ca=capitals[country]))


#--------------------------------------------------------------------------------------#

# Q 9:
"""
Print the country names and capitals by using a for loop and f-strings as follows:
'<capital> is the capital of <country>'

Expected Output:
Washington is the capital of USA
Beijing is the capital of China
Berlin is the capital of Germany
London is the capital of UK
"""

# S 9:

# for country, city in capitals.items():
#     print(f'{city} is the capital of {country}')


# --------------------------------------------------------------------------------------#

# Q 10:
"""
Print the country names and capitals by using Comprehension and f-strings as follows:
'<capital> is the capital of <country>'

Expected Output:
Washington is the capital of USA
Beijing is the capital of China
Berlin is the capital of Germany
London is the capital of UK
"""

# S 10:

[
    print(f'{city} is the capital of {country}')
    for country, city in capitals.items()
]


# --------------------------------------------------------------------------------------#

