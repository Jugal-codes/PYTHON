'''
STAR PYRAMID 
      *
    * * *
  * * * * * 
* * * * * * *
'''
num = int(input("Enter number:"))

for i in range(1, num+1):

    for j in range(1, num-i+1):
        print(" ", end=" ")

    for j in range(1, i+1):
        print("*", end=" ")

    for j in range(2,i+1):
        print("*", end=" ")

    print()


'''
REVERSE STAR PYRAMID
* * * * * * *
  * * * * *
    * * *
      *
'''
num = int(input("enter num:"))

for i in range(num,0,-1):

    for j in range(1,num-i+1):
        print(" ", end = " ")

    for j in range(1,i+1):
        print("*", end = " ")

    for j in range(2,i+1):
        print("*", end = " ")

    print()



'''
NUMBER PYRAMID
      1
    1 2 3
  1 2 3 4 5 
1 2 3 4 5 6 7
'''
num = int(input("Enter number:"))

for i in range(1, num+1):

    for j in range(1, num-i+1):
        print(" ", end=" ")

    for j in range(1, 2*i):
        print(j, end=" ")

    print()



'''
ALPHABET PYRAMID
      A
    A B C
  A B C D E 
A B C D E F G
'''
num = int(input("ENter a number:"))

for i in range(1,num+1):

    for j in range(1,num-i+1):
        print(" ", end=" ")

    for j in range(1, 2*i):
        print(chr(64+j), end=" ")

    print()



'''
PALINDROME NUMBER PYRAMID
      1
    1 2 1
  1 2 3 2 1 
1 2 3 4 3 2 1 
'''
num = int(input("Enter a number:"))

for i in range(1,num+1):

    for j in range(1, num-i+1):
        print(" ", end=" ")

    for j in range(1, i+1):
        print(j, end=" ")

    for j in range (i, 1, -1):
        print(j-1, end=" ")

    print()



'''
PALINDROME ALPHABET PYRAMID
      A
    A B A
  A B C B A 
A B C D C B A
'''
num = int(input("Enter a number:"))

for i in range(1,num+1):

    for j in range(1, num-i+1):
        print(" ", end=" ")

    for j in range(1, i+1):
        print(chr(64+j), end=" ")

    for j in range (i, 1, -1):
        print(chr(64+j-1), end=" ")

    print()


'''
STAR DAIMOND
      *
    * * *
  * * * * * 
* * * * * * *
  * * * * *
    * * *
      *
'''
num = int(input("Enter number:"))

# For upper pyramid
for i in range(1, num+1):

    for j in range(1, num-i+1):
        print(" ", end=" ")
    for j in range(1, i+1):
        print("*", end=" ")
    for j in range(2,i+1):
        print("*", end=" ")

    print()

# For lower pyramid
for i in range(num-1,0,-1):

    for j in range(1,num-i+1):
        print(" ", end = " ")
    for j in range(1,i+1):
        print("*", end = " ")
    for j in range(2,i+1):
        print("*", end = " ")

    print()


