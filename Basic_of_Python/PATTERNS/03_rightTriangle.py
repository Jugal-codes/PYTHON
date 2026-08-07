'''
RIGHT STAR TRIANGLE
      *
    * *
  * * * 
* * * *
'''
num = int(input("enter num:"))

for i in range(1,num+1):

    for j in range(1,num-i+1):
        print(" ", end = " ")

    for j in range(1,i+1):
        print("*", end = " ")

    print()



'''
REVERSE RIGHT TRIANGLE
* * * * 
  * * * 
    * * 
      *
'''
num = int(input("enter num:"))

for i in range(num,0,-1):

    for j in range(1,num-i+1):
        print(" ", end = " ")

    for j in range(1,i+1):
        print("*", end = " ")

    print()



'''
ALPHABET RIGHT TRIANGLE
      A
    A B
  A B C
A B C D 
'''
num = int(input("enter num:"))

for i in range(1,num+1):

    for j in range(1,num-i+1):
        print(" ", end = " ")

    for j in range(1,i+1):
        print(chr(64+j), end = " ")
        
    print()




