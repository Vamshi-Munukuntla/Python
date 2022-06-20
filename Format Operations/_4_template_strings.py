"""
4 - Template Strings

* Template class under 'string' module
* $ is the place holder

"""

from string import Template

# Ex 1
name = "Bruce Wayne"
hero = 'Batman'

template = Template("$H is $N.")
print(template.substitute(H=hero, N=name))

# Ex 2
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

result = num1*num2
statement = Template("$N1 multiplied by $N2 equals to $R")
print(statement.substitute(N1=num1, N2=num2, R=result))

