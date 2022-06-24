"""
Super Class
    -   Child Class 1
    -   Child Class 2
"""


class SuperClass:
    # Super Class properties
    pass


class ChildClass1(SuperClass):
    # super class properties'
    # child class 1 properties'
    pass


class ChildClass2(SuperClass):
    # super class properties'
    # child class 2 properties'
    pass


# Ex
# superclass -> Shape


import math


class Shape(object):
    # Super class
    def __init__(self, color='red'):
        self.color = color


class Circle(Shape):
    # Subclass -> derives from Super class
    # Circle inherits from Shape.
    def __init__(self, radius=5.0 , color='Sky-Blue'):
        super().__init__(color=color)
        self.radius = radius

    def area(self):
        return math.pi * (self.radius**2)


class Rectangle(Shape):
    # Rectangle inherits from Shape

    def __init__(self, length=5.0, breadth=1.0, color='Orange'):
        super().__init__(color=color)
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Square(Shape):

    def __init__(self, side=1.0, color = 'white'):
        super().__init__(color)
        self.side = side

    def area(self):
        return self.side**2


# Create Objects

# Shape
sh = Shape('Magenta')
print(f'Color of shape is {sh.color}.')
print()

print('----------CIRCLE--------------')
print()

# Circle
ci = Circle(radius=5.75, color='Saffron')
print(f'Color of Circle is {ci.color}.')
print(f'Radius of Circle is {ci.radius} meters.')
print(f'Area of Circle is {ci.area()} square meter.')
print()

print('----------RECTANGLE--------------')
print()

# Rectangle
re = Rectangle(length=71.789, breadth=45.45, color='Dark Grey')
print(f'Color of the Rectangle is {re.color}.')
print(f'Area of the Rectangle is {re.area()} square meter.')
print()

"""
The 'object' class:
'object' class is the super class of all classes.
It is also called as Root Class

All the classes, either Explicitly or Implicitly, derived from this 'Object' class.

class SuperClass(object) == class SuperClass:
"""


print('Is Shape a subclass of object class?', isinstance(sh, object))

# is subclass()
# is Square Class is subclass of Shape Class
print('Is Square class is subclass of Shape Class?:', issubclass(Square, Shape))











