"""
When a class inherits from multiple classes, it's called Multiple Inheritance.
"""


class MainClass1:
    pass


class MainClass2:
    pass


class SubClass(MainClass1, MainClass2):
    pass


# Create class Clock, and Calendar -> CalendarClock will inherit from both classes

class Clock:
    """"
    Simulates the time
    """
    def __init__(self, hours, minutes, seconds):
        self.set_clock(hours, minutes, seconds)

    def set_clock(self, new_hour, new_minute, new_second):
        self.__hours = new_hour
        self.__minutes = new_minute
        self.__seconds = new_second

    def time(self):
        return f'new time is: {self.__hours}:{self.__minutes}:{self.__seconds}'


clock = Clock(0, 0, 0)
print(clock.time())
clock.set_clock(4, 5, 3)
print(clock.time())


class Calendar:
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


print()
print('----------------calendar---------------')
calendar = Calendar(4, 12, 1997)
calendar.set_calendar(5, 12, 1997)
print(calendar.date())


# CalendarClock Class
class CalendarClock(Clock, Calendar):
    """
    Keeps calendar and clock together.
    """
    def __init__(self, day, month, year, hours, minutes, seconds):
        # call the super classes init methods
        Clock.__init__(self, hours, minutes, seconds)
        Calendar.__init__(self, day, month, year)


print()
print('---------------Calendar Clock-------------------')
calendar_clock = CalendarClock(8, 6, 2014, 3, 15, 45)
print(calendar_clock)
print(calendar_clock.date())
print(calendar_clock.time())

















