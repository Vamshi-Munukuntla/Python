# ------------------ OOP BASICS -------------------- #

"""
Object-Oriented Programming (OOP)

In Python Objects have:
* attributes
* behaviours


Example:
    Penguin
* Attributes : name, age, height, weight, family, color
* Behaviours : walk, swim, dance, sing....

OOP : Prevents code repetition
DRY : Do not Repeat Yourself
"""

"""
Class:
A class is a blueprint for creating objects.
It is the template for creating objects.
It tells how the objects are going to look like.

Example:
    A House is an object, the architectural drawing of that house is the class.
"""

"""
We use 'class' keyword to create a class.
The name of our class is Penguin.
"""


class Penguin:
    pass


"""
Object:
An object is an instance of the class.
Instantiate: Creating Objects from Classes.
We create Object by CALLING Classes.
"""

# Create a Penguin Object -> peng
peng = Penguin()
# print(peng)

"""
Class Attribute:

The attribute that all the Penguins have.
Ex: Scientific Family -> Spheniscidae (It's same for all the penguins).
So all the penguins are from Spheniscidae family.


Instance Attribute:

It differs from one object to another object.
Ex: Penguin -> age, color, name, height
"""

"""
Method:
Methods are Functions defined in a Class.
Methods are behaviours of the object.
"""


class Penguin:
    # Class Attributes
    family = 'Spheniscidae'

    # Instance Attributes
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color


"""
self: the current object that being created.
"""

# Create two Penguin Objects
king = Penguin('King Penguin', 4, 'Orange')
yellow_eyed = Penguin('Yellow-eyed Penguin', 1, 'Brown')

"""
To get Attributes -> '.'
    * Class Attributes -> .__class__.
    * Instance Attributes -> .
"""


# print the class attributes
# print('Scientific Family of {0} is {1}.'.format(king.name, king.__class__.family))
# print('Scientific Family of {0} is {1}.'.format(yellow_eyed.name, yellow_eyed.__class__.family))

"""
__init__(self, ......):
When we create an object from a class the first method that get called is __init__() method.
It is called the 'constructor' method.
__init__() creates the instances.

* self: refers the current object that being created.
Attributes:
    self.name  = ....
    self.age   = ....
    self.color = ....
"""

# print the Instance Attributes

# Age
# print('Age of {0} is {1}.'.format(king.name, king.age))
# print('Age of {0} is {1}.'.format(yellow_eyed.name, yellow_eyed.age))

# Color
# print('Color of {0} is {1}.'.format(king.name, king.color))
# print('Color of {0} is {1}.'.format(yellow_eyed.name, yellow_eyed.color))


# Add Methods to our Penguin class
class Penguin:

    # Class Attributes
    family = 'Spheniscidae'

    # Instance Attributes
    # Constructor
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    # methods - Behaviours
    # first_parameter -> self
    def swim(self):
        return f'{self.name} can swim.'

    def sing(self, can_sing=False):
        if can_sing:
            return f'{self.name} can sing.'
        else:
            return f'{self.name} cannot sing.'

    def dance(self, can_dance=False):
        if can_dance:
            return f'{self.name} can dance.'
        else:
            return f'{self.name} cannot dance.'


# ----------------- Object 1 - Rockhopper --------------------#

# # Create new Penguin objects
# rockhopper = Penguin('Rockhopper', 8, 'Yellow-Brown')
#
# # Can Rockhopper swim
# # rockhopper.swim() -> Penguin.swim(rockhopper)
# print(rockhopper.swim())
#
# # Can Rockhopper sing
# print(rockhopper.sing(True))
#
# # Can Rockhopper Dance
# print(rockhopper.dance(False))
# # print(rockhopper.dance())
# # print(rockhopper.dance(can_dance=False))

# ----------------- Object 2 - Happy Feet --------------------#

# Create new Penguin objects
# happy_feet = Penguin('Happy Feet', 8, 'Yellow-Brown')
#
# # Can happy_feet swim
# # happy_feet.swim() -> Penguin.swim(happy_feet)
# print(happy_feet.swim())
#
# # Can happy_feet sing
# print(happy_feet.sing(False))
#
# # Can happy_feet Dance
# print(happy_feet.dance(True))


# -------------------------- INHERITANCE -------------------------#

"""
Inheritance:
Classes can inherit from other classes. (Like in real world.)

Parent Class -> class that is inherited by Child Class.
Child  Class -> class that inherits from Parent Class.

Parent Class -> Super Class (Base Class)
Child Class -> Derived Class
"""

# Define Bird Class
class Bird:

    def __init__(self):
        print('Bird Class is created.')

    def Who_Am_I(self):
        print("I am a Bird.")

    def fly(self):
        print("I can fly.")

    def swim(self):
        print('I can swim.')


# Create a Bird Instance
# birdy = Bird()
# birdy.Who_Am_I()
# birdy.swim()
# birdy.fly()


# We have a Parent Class for all bird types
# Owl is a bird, so it is a child class

# Child class
class Owl(Bird):

    def __init__(self):
        # First-> We call __init__() of Super class (super() == Bird)
        super().__init__()
        print('Owl is Created.')

    # Override the parent methods
    def Who_Am_I(self):
        print('I am an Owl.')

    # Since all the birds can fly -> Owl also can fly.
    # Leave fly method as it is -> don't override

    def swim(self):
        print("Owls can't swim")

    # Owls have night vision
    def night_vision(self):
        print('Yup, I have night vision.')
        print('I watch you.')


# Create an Owl Instance
# barn_owl = Owl()
# print(barn_owl)
# barn_owl.Who_Am_I()
# barn_owl.fly()
# barn_owl.swim()
# barn_owl.night_vision()


# -------------------------------- ENCAPSULATION ---------------------------- #
"""
Encapsulation (Information Hiding):

We may not want anyone to access the attributes in our class.
We may want to control the access.
Encapsulation provides information hiding.

Attribute hiding: is done via '__'
Attributes with '__' prefix (__<attr_name>) becomes Private.

Private means, it can only accessible inside the class.
"""

# Let's assume we have a Telephone class


class Telephone:

    def __init__(self):
        # Let's define the standard price of the telephone. -> private attribute
        self.__price = 1000

    def sell(self):
        print(f'Selling Price is: ${self.__price}')

    # getter
    def set_price(self, new_price):
        if new_price <= 0:
            print('Price must be POSITIVE.')
        else:
            self.__price = new_price

    # setter
    def get_price(self):
        return self.__price


# create a Telephone object
phone = Telephone()

# We want to access its price
# AttributeError: 'Telephone' object has no attribute '__price'
# __price is Private

# phone.__price()

# # sell the phone
# phone.sell()    # $1000
#
# # sell the price -> $5000
# phone.__price = 5000
#
# # sell the phone
# phone.sell()    # $1000
# again we see as $1000 -> because we didn't set the __price in the class.
# phone.__price -> Python creates a new attribute

# print(phone.__price)
#
# """
# In Python,
# You can set attributes to the objects, independent of their classes.
# """
# phone.color = 'Yellow'
# print(phone.color)
#
# # How do we set the price.
# """
# Get-Set Methods -> Getter-Setter
# We use them to set and get the Private Attributes of a class.
# """
#
# # set the price to $8000
# phone.set_price(8000)
#
# price = phone.get_price()
# print("New Price is $", price)
#
# # sell the phone
# phone.sell()
#
#
# phone.set_price(-2000)
# price = phone.get_price()
# # sell the phone
# phone.sell()
# print("New Price is $", price)


# ----------------------------  POLYMORPHISM --------------------- #

"""
Polymorphism:
(many forms)
It refers to the same object (or function) exhibiting different forms and behaviours.
"""

# Define Bird Class (PARENT CLASS)
class Bird:

    def __init__(self):
        print('Bird Class is created.')

    def Who_Am_I(self):
        print("I am a Bird.")

    def fly(self):
        print("I can fly.")

    def swim(self):
        print('I can swim.')


# Owl class (CHILD CLASS)
class Owl(Bird):

    def __init__(self):
        # First-> We call __init__() of Super class (super() == Bird)
        super().__init__()
        print('Owl is Created.')

    # Override the parent methods
    def Who_Am_I(self):
        print('I am an Owl.')

    # Since all the birds can fly -> Owl also can fly.
    # Leave fly method as it is -> don't override

    def swim(self):
        print("Owls can't swim")

    # Owls have night vision
    def night_vision(self):
        print('Yup, I have night vision.')
        print('I watch you.')


# Penguin class
class Penguin(Bird):

    def __init__(self):
        super().__init__()
        print('Penguin class is created.')

    # Override the parent methods
    def Who_Am_I(self):
        print('I am an Penguin.')

    def fly(self):
        print('I cannot fly.')

    # leave the swim method as it is.

# Two Child classes from the same parent class
# Owl, Penguin  <----- Bird


# Common Function
def can_it_fly(any_bird):
    # call the fly method on the parameter bird
    any_bird.fly()


# call with three objects -> Bird, Owl, Penguin
any_bird = Bird()
snowy_owl = Owl()
King_penguin = Penguin()

print('---------------FLY TEST--------------')
can_it_fly(any_bird)
can_it_fly(snowy_owl)
can_it_fly(King_penguin)


"""
The same function can_it_fly returns different results
based on the object as its parameter.
"""












