'''
The math module in Python provides built-in mathematical functions for:
    Square roots, Powers, Trigonometry, Logarithms, Rounding, Constants like π and e

It works with numbers, not strings or lists.
'''

# Way of import math madule
'''
1. import only 1 function from math module
from math import pow

2. import more than 1 function from math module
from math import pow, sqrt

3. Can give alias to function
from math import pow as p, sqrt

4. import all func from math module
from math import *

print(pow(2, 5))
print(sqrt(25))
print(ceil(3.4))
'''

# PART - 1
import math

# Important constants :
math.pi     # 3.141592653589793
math.e      # 2.718281828459045

# Power & root functions :
print(math.sqrt(25))   # 5.0
print(math.cbrt(27))   # 3.0
print(math.pow(2, 3))  # 8.0

# Rounding functions :
math.ceil(4.2)    # 5
math.floor(4.9)   # 4
math.trunc(4.9)   # 4

# GCD & factorial :
math.gcd(12, 18)     # 6
math.factorial(5)    # 120

# Absolute & remainder :
math.fabs(-5.4)     # 5.4
math.fmod(10, 3)    # 1.0

# Logarithmic functions :
math.log(10)        # Natural log
math.log10(100	)   # Base 10 log
math.log2(8)        # Base 2 log



# PART - 2
import math as m

print(m.pi)        # 3.141592653589793
# print(math.pi)   # ERROR

print(m.ceil(3.4))   # 4
print(m.ceil(-2.4))  # -2

print(m.floor(3.4))  # 3
print(m.floor(-2.4)) # -3


# trunc is math module's function AND round is python's function
print(m.trunc(1.22))    # 1 
print(m.trunc(22.757))  # 22 

print(round(3.4)) # 3
print(round(3.5)) # 4
print(round(22.757)) # 23

print("--------------")
# 12 -> 1,2,3,4,6,12
# 18 -> 1,2,3,6,9,18
print(m.gcd(12, 18))   # 6
print(m.lcm(12, 18))   # 36

print(m.factorial(5))   # 120
print(m.factorial(20))  # 2432902008176640000

# fabs -> |-3.4| = 3.4
print(m.fabs(-3.4))     # 3.4

# fmod -> find module with float value also
print(m.fmod(4, 2))     # 0.0
print(m.fmod(3.1, 2))   # 1.1

# infinite value
x = float("-inf")
y = float("inf")

print(y > 10000000000000000000000000000000000000000000000000000000000000000000000000)   # True
print(y < 10000000000000000000000000000000000000000000000000000000000000000000000000)   # False
