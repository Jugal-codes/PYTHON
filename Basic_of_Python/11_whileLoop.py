# while Loop : this loop runs as long as a condition is true.
# Syntax :
'''
while condition:
    # code to execute
'''

# Print 1 to 5 number
count = 1
while count <= 5:
    print(count)
    count += 1



# Reverse counting
count = 10
while count >= 1:
    print(count)
    count -= 1



# Sum of n number
n = int(input("Enter a number:"))
count = 1
sum = 0

while count <= n:
    sum += count
    count += 1

print(f"Sum of 1 to {n} is: {sum}")



# Sum of Digit
num = int(input("Enter a number:"))
num1 = num
sum = 0
count = 0

while num > 0:
    count = num % 10
    sum += count
    num = num // 10

print(f"sum of {num1}'s digit is: {sum}")



# Count Digits
# Enter number: 23456
# Number of digits = 5

num = int(input("Enter a number:"))
num1 = num
digit = 0

while num > 0:
    count = num % 10
    digit += 1
    num = num // 10
    
print(f"Total digit in {num1} is: {digit}")

