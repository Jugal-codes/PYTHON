# for Loop : when you know how many times you want to repeat something
#  Syntax :
'''
for variable in sequence:
    # code to execute
'''



# 5 is stop point bt 5 is not inculded (exclusive) -> print 0 to 4

for i in range(5): 
    print(i)



# 1 is start point nd 5 is stop point -> print 1 to 4

for i in range(1, 5): 
    print(i)



# 1 is start, 10 is end, 2 is step (By default it was 1) -> print 1, 3, 5, 7, 9

for i in range(1, 10, 2): 
    print(i)
  


# Take number from user nd print 1 to n
n = int(input("Enter ur number:"))

for i in range(1, n+1):
    print(i)
 


# Print table of number - take a number from user
num = int(input("Enter ur number:"))

for i in range(1,11):
    print(num, " * ", i ," = ", num*i)

  


# Print 2^4 --> 16 using for loop
base = int(input("Enter a base:"))
expo = int(input("Enter a expo:"))
ans = 1

for i in range(1, expo+1):
    ans = ans * base
print("Ans: ", ans)



# How much time loop will be execute...
for i in range(1,6):
    for j in range(1,4):
        print("i =",i , "j =", j, end = " | ")
    print()

