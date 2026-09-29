
import datetime as d


# 1. Get Current Date
today = d.date.today()
print(today)
# OR
print(d.date.today())

# 2. Get Current Date and Time
now = d.datetime.now()
print(now)
# OR
print(d.datetime.now())


# 3. Create Your Own Date
dt = d.date(2026, 2, 8)
print(dt)


# 4. Create Your Own Date and Time
date_time = d.datetime(2025, 12, 1, 15, 30, 45)
print(date_time)


# 5. Get Day, Month, Year
today = d.date.today()

print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)


# 6. Get Hour, Minute, Second, Microsecond
t = d.datetime.now()

print("Hour :", t.hour)
print("Minute :", t.minute)
print("Second :", t.second)
print("MicroSecond :", t.microsecond)


# 7. Add Days to Date
today = d.date.today()
new_date = today + d.timedelta(days=5)

print(new_date)


# 8. Find Difference Between Two Dates
d1 = d.date(2026, 2, 8)
d2 = d.date(2026, 2, 1)

diff = d1 - d2
print(diff.days)


# 9. Get Only Current Time
time_now = d.datetime.now().time()
print(time_now)


# 10. Convert String to Date (strptime)
date_string = "08-02-2026"
date_obj = d.datetime.strptime(date_string, "%d-%m-%Y")

print(date_obj)



# 11. Format Date
# today = d.date.today()
# print(today.strftime("%d-%m-%Y"))

'''
Common formats for date and time:

%d  → Day (01-31)
%m  → Month (01-12)
%Y  → Full Year (2026)
%y  → Short Year (26)

%A  → Full Day name (Sunday)
%a  → Short Day name (Sun)

%B  → Full Month name (February)
%b  → Short Month name (Feb)

%H  → Hour (00-23)  [24-hour format]
%I  → Hour (01-12)  [12-hour format]

%p  → AM/PM

%M  → Minutes (00-59)
%S  → Seconds (00-59)

%f  → Microseconds (000000-999999)

%j  → Day number of year (001-366)

%U  → Week number of year (Sunday as first day)
%W  → Week number of year (Monday as first day)

%c  → Full date and time
%x  → Date only
%X  → Time only
'''


# 11. Convert Date to String (strftime)
t = d.datetime.now()
print(t)

print(t.strftime("%d-%m-%Y"))   # 10-09-2026
print(t.strftime("%d-%m-%y"))   # 10-09-26

print(t.strftime("%A"))     # Thursday
print(t.strftime("%a"))     # Mhu

print(t.strftime("%B"))     # September
print(t.strftime("%b"))     # Sep

print(t.strftime("%H %p"))  # 18 PM
print(t.strftime("%I %p"))  # 06 PM

print(t.strftime("%H:%M:%S.%f"))    # 18:50:59.307650

print(t.strftime("%j")) # 253 days
print(t.strftime("%U")) # 36 weeks (Week start from sunday)
print(t.strftime("%W")) # 36 weeks (Week start from monday)

print(t.strftime("%c")) # Thu Sep 10 18:50:59 2026
print(t.strftime("%x")) # 09/10/26
print(t.strftime("%X")) # 18:50:59


# 12. convert string to date -> strptime
date_string = "08-02-2026"
# date_obj = d.datetime.strptime(date_string) #ERROR -> date_obj = d.datetime.strptime(date_string)
date_obj = d.datetime.strptime(date_string, "%d-%m-%Y")
print(date_obj) # 2026-02-08 00:00:00

















