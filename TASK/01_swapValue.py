# For swapping values of two variables we can use temporary variable
a = 5
b = 10
print("Before swapping: a =", a, "b =", b) #Before swapping: a = 5 b = 10

# Case 1: Using temporary variable
temp = a
a = b
a = temp
print("After swapping, In Case 1: a =", a, "b =", b) #After swapping: a = 10 b = 10

# Case 2: Without using temporary variable
a = a + b #a = 5 + 10 = 15
b = a - b #b = 15 - 10 = 5
a = a - b #a = 15 - 5 = 10
print("After swapping, In Case 2: a =", a, "b =", b) #After swapping: a = 10 b = 5

# Case 3: Using tuple unpacking
a, b = b, a
print("After swapping, In Case 3: a =", a, "b =", b) #After swapping: a = 5 b = 10
