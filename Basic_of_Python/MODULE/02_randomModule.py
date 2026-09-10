
# PART - 1

import random as r
import math as m

# 1. random.random() : Generates a float number between 0.0 and 1.0 (exclusive)
print(r.random())

# Gives random float num 1.0 to 11.0 (exclusive)
print(r.random() * 11)

# Convert float into int using m.truc() 
print(m.trunc(r.random() * 11))

# Convert float into int using typecasting - int() 
print(int(r.random() * 11))



# 2.random.randint(a, b) : Generates a random integer between a and b (inclusive)
print(r.randint(1, 6))      # 6 inclusive
print(r.randint(1, 10))     # 10 inclusive
# print(r.randint(10, 1))   # Error



# 3. random.randrange(start, stop, step) : Works like range() but returns one random value
print(r.randrange(1, 10))
print(r.randrange(0, 10, 2))



# 4. random.choice() : Selects one random element from a list
colors = ["Red", "Green", "Blue"]
print(r.choice(colors))



# 5. random.choices() : Selects multiple elements (repetition allowed)
colors = ["Red", "Green", "Blue"]
print(r.choices(colors, k=3))



# 6. random.sample() : Selects multiple UNIQUE elements (no repetition)
numbers = [1, 2, 3, 4, 5]
print(r.sample(numbers, 3))
# print(r.sample(numbers, k=8))  #ERROR



# 7. random.shuffle() : Randomly changes the order of list elements
nums = [1, 2, 3, 4, 5]
r.shuffle(nums)
print(nums)



# 8. random.uniform(a, b) : Generates a random float number between a and b
print(r.uniform(1.5, 5.5))   # 5.5 exclusive

