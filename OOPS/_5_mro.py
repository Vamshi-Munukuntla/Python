"""
MRO (Method Resolution Order)
"""

"""
Multiple Level Inheritance:
GrandParent -> Parent -> Child
"""


class GrandParent:
    # GrandParent properties
    pass


class Parent(GrandParent):
    # GrandParent Properties
    # Parent Properties
    pass


class Child(Parent):
    # GrandParent Properties
    # Parent Properties
    # Child Properties
    pass

# SandWatch -> Clock
# Clock and Calendar -> ClockCalendar


class SandWatch:
    def __init__(self):
        self.start_sand_watch()

    def start_sand_watch(self):
        print('SandWatch Started.')


# Create class Clock, and Calendar -> CalendarClock will inherit from both classes
class Clock(SandWatch):
    """"
    Simulates the time
    """
    def __init__(self, hours, minutes, seconds):
        super().__init__()
        self.set_clock(hours, minutes, seconds)

    def set_clock(self, new_hour, new_minute, new_second):
        self.__hours = new_hour
        self.__minutes = new_minute
        self.__seconds = new_second

    def time(self):
        return f'new time is: {self.__hours}:{self.__minutes}:{self.__seconds}'

    # over-ride start_sand_watch
    def start_sand_watch(self):
        print('SandWatch Started in Clock Class.')


# Calendar Class
class Calendar(object):
    """
    Simulates the Calendar
    """
    def __init__(self, day, month, year):
        self.set_calendar(day, month, year)

    def set_calendar(self, day, month, year):
        self.__day = day
        self.__month = month
        self.__year = year

    def date(self):
        return f"dd/mm/yyyy: {self.__day}/{self.__month}/{self.__year}"


# CalendarClock Class
class CalendarClock(Clock, Calendar):
    """
    Keeps calendar and clock together.
    """
    def __init__(self, day, month, year, hours, minutes, seconds):
        # call the super classes init methods
        Clock.__init__(self, hours, minutes, seconds)
        Calendar.__init__(self, day, month, year)


# CalendarClock
calendar_clock = CalendarClock(12, 8, 2020, 3, 12, 45)

"""
Question: If we have the same method in different classes which one will be executed?
Answer:    It will execute the nearest one.
Method Resolution Order -> MRO.
"""

# MRO
print('MRO:', CalendarClock.__mro__)
for m in CalendarClock.__mro__:
    print(m)










