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
def day_names(day):

    days = (day, len(day))

    return print("%s has %s letters" % days)


day_names('Sunday')


# --------------------------------------------------------------------------------------#

# Q 2:
"""
Call the function in Q1 and print the result with str.format() as follows:
'day: Monday, length: 6'
"""

# S 2:




#--------------------------------------------------------------------------------------#

# Q 3:
"""
Call the function in Q1 and print the result with f-strings as follows:
'day: Monday, length: 6'
"""

# S 3:




#--------------------------------------------------------------------------------------#

# Q 4:
"""
Call the function in Q1 and print the result with Template Strings as follows:
'day: Monday, length: 6'
"""

# S 4:




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

print('The capital city of USA is %(USA)s' % capitals)



#--------------------------------------------------------------------------------------#

# Q 6:
"""
Use the capitals dictionary and str.format() to print as follows:
"The capital city of Germany is Berlin"
Both 'Germany' and 'Berlin' will be variables.
"""

# S 6:
country = 'Germany'
statement = 'The capital city of {0} is {1}'
print(statement.format(country, capitals[country]))


#--------------------------------------------------------------------------------------#

# Q 7:
"""
Use the capitals dictionary and f-strings to print as follows:
"The capital city of UK is London"
Both 'UK' and 'London' will be variables.
"""

# S 7:

country = 'UK'
print(f'The capital city of {country} is {capitals[country]}')


#--------------------------------------------------------------------------------------#

# Q 8:
"""
Use the capitals dictionary and Template Strings to print as follows:
"The capital city of USA is Washington"
Both 'USA' and 'Washington' will be variables.
"""

# S 8:
from string import Template

country = 'USA'
template = Template("The capital city of $C is $Cc")
print(template.substitute(C=country, Cc=capitals[country]))


# --------------------------------------------------------------------------------------#

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

for i in capitals:
    print(f"{capitals[i]} is the capital of {i}")


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




# --------------------------------------------------------------------------------------#

