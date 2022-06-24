# Defining a class
# Docstring

class Car:

    """
    This is the car class.
    """
    # Class Attribute
    brand = 'BMW'

    def work(self):
        print('This car works.')


# to call the brand attribute
# print(Car.brand)

"""
dunder (double underscore)
Methods or attributes with two underscore prefix. -> __<attribute_name>
There are built-in dunder methods.
"""

# docstring of class
# print(Car.__doc__)

# Class Name
# print(Car.__name__)

# Get details of work method
# print(Car.work)
#
# X_series = Car()
# X_series.work()
# print(X_series.brand)

"""
Question:
Where is the 'self' parameter?
X_series.work()


Answer:
'self' parameter is X_series itself.
"""

# First Parameter is 'self' -> X_series
# Car.work(X_series)
# X_series.work()
# Car.work(self=X_series)
# # All the three provides the same result.

import math
# Circle Class


class Circle:

    def __init__(self, radius):
        self.__radius = radius

    # Get the radius
    def get_radius(self):
        return f'Radius of the Circle is : {self.__radius}'

    # Set the new radius
    def set_radius(self, new_radius):
        if new_radius > 0:
            self.__radius = new_radius
            print(f'New Radius of the circle is {self.__radius}.')
        else:
            print('Radius must be positive.')

    # Perimeter of the circle
    def perimeter(self):
        return f'Perimeter of the circle with radius {self.__radius} is : {math.pi * self.__radius*2}'


# Create object
# circle_1 = Circle(10)
# print(circle_1.get_radius())
#
# perimeter = circle_1.perimeter()
# print(perimeter)
# print()
#
# print("---------set-----------")
# print()
# circle_1.set_radius(15)
#
# perimeter = circle_1.perimeter()
# print(perimeter)


# Define a New Class -> Student Class
class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


student_1 = Student('Vamshi', 24, '9th Grade')
print(student_1.name)
print(student_1.age)
print(student_1.grade)
print()

print('-----------delete---------')

print()
del student_1.age
# AttributeError: 'Student' object has no attribute 'age'
# print(student_1.age)

"""
Delete Attributes:
del object.attribute

Delete Object:
del object
"""

# Delete student_1 object
del student_1

# NameError: name 'student_1' is not defined.
# print(student_1) # -> This gives error







