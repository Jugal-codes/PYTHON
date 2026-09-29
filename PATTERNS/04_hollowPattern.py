'''
HOLLOW SQUARE
* * * * *
*       *
*       *
*       *
* * * * *
'''
num = int(input("Enter a number : "))

for i in range(1,num+1):

    for j in range(1,num+1):
        if i==1 or i==num or j==1 or j==num:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()



'''
STAR PLUS - (n ALWAYS ODD)
1 2 3 4 5
    *       1
    *       2
* * * * *   3
    *       4
    *       5
'''
num = int(input("Enter a number:"))

for i in range(1,num+1):

    for j in range(1,num+1):
        if i == num // 2 + 1 or j == num // 2 + 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()



'''
STAR CROSS - (n ALWAYS ODD)
    1 2 3 4 5 
1   *       *
2     *   *  
3       *
4     *   *
5   *       *
'''
num = int(input("Enter a number:"))

for i in range(1,num+1):

    for j in range(1, num+1):
        if (i+j) == 1+num or i==j:
            print("*", end = " ")
        else:
            print(" ", end = " ")

    print()


