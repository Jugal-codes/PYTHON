# Operators are special symbols that perform operations on variables and values (operands).
# Types of Operators :
# 1. Arithmetic Operators
# 2. Relational(Comparison) Operators
# 3. Logical Operators
# 4. Assignment Operators 
# 5. Bitwise Operators
# 6. Identity Operators
# 7. Membership Operators



# Arithmetic Operators
a = 5
b = 3

print(f"Addition : a + b = {a+b}")
print(f"Subtraction : a - b = {a-b}")
print(f"Multiplication : a * b = {a*b}")
print(f"Division : a / b = {a/b}")  #Gives float value
print(f"Division : a // b = {a//b}")  #Gives integer value
print(f"Modulus : a % b = {a%b}")  
print(f"Exponent : a ** b = {a**b}") 



# Relational(Comparison) Operators
print(f"Equal to : 5 == 5 {5 == 5}") # True
print(f"Equal to : 5 == 25 {5 == 25}") # False

print(f"Not equal to : 5 != 25 {5 != 25}") # True
print(f"Not equal to : 5 != 5 {5 != 5}") # False

print(f"Greater than : 5 > 3 {5 > 3}") # True

print(f"Less than : 5 < 25 {5 < 25}") # True

print(f"Equal to : 5 >= 5 {5 >= 5}") # True

print(f"Equal to : 5 <= 25 {5 <= 25}") # True


#  Logical Operators: AND OR NOT
#  AND Operator: True and True -> True, Otherwise False
#  OR Operator: False and False -> False, Otherwise True
#  NOT Operator: True <-> False

# and Operator
print(f"5 > 2 and 5 < 10: {5>2 and 5<10}")
print(f"5 < 2 and 5 < 10: {5<2 and 5<10}")
print(f"5 > 2 and 5 > 10: {5>2 and 5>10}")
print(f"5 < 2 and 5 > 10: {5<2 and 5>10}")

# or Operator
print(f"5 > 2 or 5 < 10: {5>2 or 5<10}")
print(f"5 < 2 or 5 < 10: {5<2 or 5<10}")
print(f"5 > 2 or 5 > 10: {5>2 or 5>10}")
print(f"5 < 2 or 5 > 10: {5<2 or 5>10}")

# not operator
print(f"not True: {not True}")
print(f"not False: {not False}")


# Assignment Operators
x = 5
print(f"Assign : x = 5 -> value of x is {x}")
x += 4
print(f"Add and Assign : x += 4 -> value of x is {x}")
x -= 2
print(f"Subtract and Assign : x -= 2 -> value of x is {x}")
x *= 3
print(f"Multiply and Assign : x *= 3 -> value of x is {x}")
x /= 2
print(f"Divide and Assign : x /= 2 -> value of x is {x}")   #Gives float value
x //= 2
print(f"Floor divide and Assign : x //= 2 -> value of x is {x}")    #Gives int value
x %= 3
print(f"Modulus and Assign : x %= 3 -> value of x is {x}")
x **= 3
print(f"Exponent and Assign : x **= 3 -> value of x is {x}")


# Identity Operators - Used to compare memory location.
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)     #True - same object in memory 
print(a is c)     #False - different memory location

# Membership Operators : Used to check if a value exists inside a sequence (list, string, tuple)
print("a" in "apple")   #True
print("x" in "apple")   #False
print("x" not in "apple")   #True
print("a" not in "apple")   #False

