"""
Operator Overloading
"""


class Point:
    """
    A point in Co-ordinate Axis
    """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


# Create two Point Objects
p1 = Point(6, 9)
p2 = Point(-3, 8)

print('----- Before Overloading -----')
print(p1)
# __str__() is String representation of object
print(p1.__str__())

# print() -> __str__()
# It comes from 'object' class by default
# <_6_operator_overloading.Point object at 0x000002486F0113F0>

"""
Define our own string representations -> override __str__() => Operator Overloading
"""


class Point:
    """
    A point in Co-ordinate Axis
    """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'This is a point at coordinates: {self.x}x{self.y}'


print()
print('----- After Overloading -----')
# Create two Point Objects
p3 = Point(6, 9)
p4 = Point(-3, 8)

print(p3)
print(p3.__str__())










