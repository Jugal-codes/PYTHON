# Print reverse num

for i in range(10,0,-1):
    print(i)



# Print sum of 1 to 10
sum = 0

for i in range(1,11):
    sum += i
print(sum)



# Sum of odd num nd even num
e_sum = 0
o_sum = 0

for i in range(1,11):
    if i % 2 == 0:
        e_sum += i
    else:
        o_sum += i
print("Even sum is: ", e_sum)
print("Odd sum is: ", o_sum)



# Print Factorial of given number
n = int(input("Enter ur number:"))
fact = 1

for i in range(1, n+1):
    fact *= i
print(fact)



# Print the given number is prime or not

# Approach 1: (Personally, I prefer this)
n = int(input("Enter ur number:"))
f = 0

for i in range(1,n+1):
    if n % i == 0:
        f += 1

if f == 2:
    print("Prime")
else:
    print("Not Prime")


# Approach 2:
n = int(input("Enter ur number:"))
f = 1

for i in range(1,n+1):
    if n % i == 0:
        f = 0
        break   # break → Stops the loop immediately

if f == 1:
    print("Prime")
else:
    print("Not Prime")
