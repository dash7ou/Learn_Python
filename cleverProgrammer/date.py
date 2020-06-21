import calendar
import datetime
import time

# 2 => number of character you want to show it :)
print(calendar.weekheader(2))
print()

print(calendar.month(2020, 6))
print()

# print list of days every item as list 7 days
print(calendar.monthcalendar(2020, 6))
print()

# print year calender
print(calendar.calendar(2020))


dayOfTheWeek = calendar.weekday(2020, 6, 20)
print(dayOfTheWeek)

isLeap = calendar.isleap(2020)
print(isLeap)
