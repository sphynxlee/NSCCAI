import datetime as datetime

right_now = datetime.datetime.now()
print('right_now: ', right_now, '\n')
print(right_now.day, right_now.month, right_now.year, right_now.hour, right_now.minute, right_now.second, right_now.microsecond)

dean_birthday = datetime.datetime(1971,5,18)
print('dean_birthday: ', dean_birthday, '\n')
sixteen_years = datetime.timedelta(days=365*16)
print('sixteen_years: ', sixteen_years, '\n')
dean_birthday = dean_birthday + sixteen_years
print('Dean\'s birthday was on a', dean_birthday.strftime('%A'), '\n')

my_birthday = datetime.datetime(1981, 12,22)
# total_days = dean_birthday + my_birthday
# print('Total days: ', total_days, '\n')
delta_days = dean_birthday - my_birthday
print('Delta days: ', delta_days, '\n')

dean_bdday = "May 18, 1971"
dean_bdday = datetime.datetime.strptime(dean_bdday, "%B %d, %Y")
print('dean_bdday: ', dean_bdday, '\n')

local_time = datetime.datetime.now(tz = datetime.timezone.utc)
print('local_time: ', local_time, '\n')
atlantic_time = local_time.astimezone()
print('atlantic_time: ', atlantic_time, '\n')

import pytz
atlantic_time = local_time.astimezone(pytz.timezone('America/Halifax'))
print('pytz atlantic_time: ', atlantic_time, '\n')

# my = datetime.datetime.mro()
# print('my: ', my, '\n')

import zoneinfo

print(zoneinfo.ZoneInfo)

for tz in zoneinfo.available_timezones():
    # print(tz)
    if 'Halifax' in tz:
        print(tz)
        break