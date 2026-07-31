# Type Conversion -> 
# we can convert one data type to another data type using type conversion functions like int(), float(), str(), etc.
# 2 types of type conversion -> 1. Implicit type conversion 2. Explicit type conversion


# 1. Implicit type conversion -> It is done automatically by python when we perform operations on different data types.
x = 5
y = 3.14
z = x + y
print(z) #8.14
print(type(z)) #<class 'float'>


# 2. Explicit type conversion -> It is done manually by the programmer using type conversion functions.
print(int(z)) #8 -> it will convert float to int by removing decimal part


# Example:

a = 10 #int
b = 3.14 #float

# Implicit type conversion --> Sum of int(a) + float(b) will be converted to float(c)
c = a + b 
print(c) #13.14 
print(type(c)) #<class 'float'>

# Explicit type conversion --> Convert float(c) in int(d)
d = int(c)
print(d) #13
print(type(d)) #<class 'int'>



# If string will be number then we can convert it into int or float
str_num = "100" # String

int_num = int(str_num) # Convert string to int
print(int_num) #100
print (type(int_num)) #<class 'int'>

float_num = float(str_num) # Convert string to float
print(float_num) #100.0
print(type(float_num)) #<class 'float'>
