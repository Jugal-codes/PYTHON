'''
SOLID SQUARE
* * * *
* * * *
* * * *
* * * *
'''
for i in range(1,5):
    for j in range(1,5):
        print("*", end = " ")
    print()

 
# Outer Loop -> no of Lines -> no of Rows
# Inner Loop -> no of star in each line -> no of Columns


'''
NUMER SQUARE
1 2 3 4 
1 2 3 4 
1 2 3 4 
1 2 3 4 
'''
for i in range(1,5):
    for j in range(1,5):
        print(j, end = " ")
    print()



'''
NUMER SQUARE
1 1 1 1
2 2 2 2
3 3 3 3
4 4 4 4
'''
for i in range (1,5):
    for j in range (1,5):
        print(i, end = " ")
    print()



'''
CHARACTER SQUARE
A B C D 
A B C D
A B C D
A B C D
'''
for i in range (1,5):
    for j in range(1,5):
        print(chr(64+j), end = " ")
    print()



'''
CHARACTER SQUARE
A A A A
B B B B
C C C C
D D D D
'''
for i in range(1,5):
    for j in range(1,5):
        print(chr(64+i), end = " ")
    print()



'''
RHOMBUS
    * * * * 
  * * * * 
* * * * 
'''
for i in range(4,0,-1):
    for j in range(1,i+1):
        print(" ", end = " ")
    for j in range(1,5):
        print("*", end = " ")
    print()

