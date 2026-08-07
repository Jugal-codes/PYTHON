# Reverse a Number
# Enter number: 1234
# Reverse = 4321

num = int(input("enter a number:"))
rnum = 0

while num > 0:
    ldigit = num % 10
    rnum = rnum * 10 + ldigit
    num = num // 10
    
print("Reversed number is:", rnum)



# Palindrome Number 

num = int(input("enter a number:"))
originalNum = num
rnum = 0

while num > 0:
    ldigit = num % 10
    rnum = rnum * 10 + ldigit
    num = num // 10

if originalNum == rnum:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")



# Even & Odd Digit Count
# Enter number: 1223456
# Even digits = 4
# Odd digits = 3

num = int(input("enter a number:"))
even_dgit = 0
odd_digit = 0

while num > 0:
    last_digit = num % 10

    if last_digit % 2 == 0:
        even_dgit += 1
    else:
       odd_digit += 1
    num //= 10

print(f"Even digit: {even_dgit}")
print(f"Odd digit: {odd_digit}")



# Find Largest Digit from a given number

num = int(input("enter a number:"))
largest_num = 0

while num > 0:
    last_digit = num % 10

    if last_digit > largest_num:
        largest_num = last_digit
    num //= 10

print(f"Largest number is: {largest_num}")



# Task 10: Armstrong Number
# Check whether a number is an Armstrong number.

# 153
# Because:
# 1³ + 5³ + 3³ = 153

