import datetime
import pytz

today = datetime.date.today()
print(today)

birthday = datetime.date(2000, 3, 27)
print(birthday)

daysSinceBirth = (today - birthday)
print(daysSinceBirth)

tdelta = datetime.timedelta(days=10)
print(today + tdelta)


print(today.year, today.month, today.weekday())

print(datetime.time(7, 2, 20, 15))

# datetime.date (Y, M, D)
# datetime.time (h, m, s, ms)
# datetime.datetime ( Y, M, D, h, m, s, ms)

# timezone we using pytz lib
datetime_today = datetime.datetime.now(tz=pytz.UTC)
datatime_pacific = datetime_today.astimezone(pytz.timezone('US/Pacific'))
print(datetime_today)
print(datatime_pacific)

# all timezones
for tz in pytz.all_timezones:
    print(tz)
