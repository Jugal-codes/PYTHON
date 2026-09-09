# Lambda with map, filter and reduce function

# lambda with map function
li = [1, 2, 3, 4, 5]

# print x * 2 for each ele of list 
result = list(map(lambda x: x * 2, li))
print(result)

# print even nd odd for each ele of list
r = list(map(lambda n: "Even" if n % 2 == 0 else "Odd", li))
print(r)




# lambda with filter function
li2 = [1, 2, 3, 4, 5, 6, 7, 8]

# filter only even ele of list
r = list(filter(lambda x: x % 2 == 0, li2))
print(r)

# we can print 2 list using filter func
evenOdd = [
    list(filter(lambda x: x % 2 == 0, li2)),
    list(filter(lambda x: x % 2 != 0, li2)),
]
print(evenOdd)


# lambda with reduce function
# Compulsory line : from functools import reduce -> to download reduce function from functools library
# reduce func return single value

from functools import reduce

nums = [1, 2, 3, 4, 5]

# Print sum of all ele 
s = reduce(lambda a, b: a + b, nums)
print(s)
s1 = reduce(lambda a, b: a + b, nums, 10)
print("10 added extra:",s1)

# Find max ele of list
m = reduce(lambda a, b: a if a > b else b, nums)
print(m)
