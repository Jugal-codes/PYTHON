# TASK 1 - Calculate days left for new year

# 1st approach : 
import datetime as d

today = d.date.today()
print(today)

new_year = d.date(2027, 1, 1)
print(new_year)

diff = new_year - today
print(diff.days)


# 2nd approach : 
today = d.date.today()
next_year = today.year + 1

new_year = d.date(next_year, 1, 1)
days_left = (new_year - today).days

print("Days left for New Year:", days_left)




# TASK 2 - Input Birth date and find exact age:
import datetime as dt

b_date = dt.date(2005, 2, 8)
print(b_date)

today = dt.date.today()
print(today)

age = today.year - b_date.year
print(age)
