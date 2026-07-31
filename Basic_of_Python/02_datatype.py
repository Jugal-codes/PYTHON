# No need to delcare data type in python, it is dynamically typed language
# Dynamic typing means that the type of a variable is determined at runtime, 
# and you can change the type of a variable by assigning it a new value of a different type. 

# Python has following data types built in by default, in these categories: 
# 1. Text Type: str
# 2. Numeric Types: int, float, complex
# 3. Sequence Types: list, tuple, range
# 4. Mapping Type: dict
# 5. Set Types: set, frozenset
# 6. Boolean Type: bool

# int value can be of any length, it is only limited by the amount of memory available.
num = 10000
print(num) #10000
print(type(num)) #<class 'int'> -->To check type of variable we can use type() function



# float value is a number that has a decimal point. It can also be in scientific notation, 
# with an "e" to indicate the power of 10.
pi = 3.14
print(pi) #3.14 
print(type(pi)) #<class 'float'>

# Scientific notation -> "e" to indicate the power of 10.
max_load = 3.5e5       # 3.5 * 10^5 = 350000.0



# Boolean value can be either True or False. It is often used in conditional statements and loops to control the flow of the program.
isActive = True
print(isActive) #True
print(type(isActive)) #<class 'bool'>



# String is a sequence of characters enclosed in single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).
name = "Jugl"
print(name) #Jugl
print(type(name)) #<class 'str'>



# List is an ordered collection of items that can be of different types. 
# It is defined using square brackets [] and items are separated by commas.
list = ["apple", "banana", "cherry"]
print(list) #['apple', 'banana', 'cherry']
print(type(list)) #<class 'list'>



# Tuple is an ordered collection of items that can be of different types, 
# but it is immutable, meaning that once it is created, its contents cannot be changed.
# It is defined using parentheses () and items are separated by commas.
tuple = ("apple", "banana", "cherry")
print(tuple) #('apple', 'banana', 'cherry')
print(type(tuple)) #<class 'tuple'>



# Dictionary is an unordered collection of key-value pairs. 
# It is defined using curly braces {} and each key is separated from its value by a colon (:), 
# and items are separated by commas.
dict = {"name": "John", "age": 30, "city": "New York"}
print(dict) #{'name': 'John', 'age': 30, 'city': 'New York'}
print(type(dict)) #<class 'dict'>



# Set is an unordered collection of unique items. It is defined using curly braces {} and 
# items are separated by commas.
set = {"apple", "banana", "cherry"}
print(set) #{'banana', 'cherry', 'apple'}
print(type(set)) #<class 'set'>



# We can identify multiple variable in one line
a, b, c = 1, "Hello", 3.14
print(a) #1
print(b) #Hello
print(c) #3.14

# We can store one value in  multiple variable
x = y = z = 10
print(x) #10
print(y) #10
print(z) #10


