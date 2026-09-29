'''
STAR TRIANGLE
*
* *
* * * 
* * * *
'''
for i in range(1,5):
    for j in range(1,i+1):
        print("*" , end = " ")
    print()



'''
REVERSE STAR TRIANGLE
* * * *
* * *
* *
*
'''
for i in range(4,0,-1):
    for j in range(1,i+1):
        print("*", end = " ")
    print()


'''
FLOYD's TRIANGLE (1 to N)
1
2 3 
4 5 6
7 8 9 10
'''
n = 1
for i in range (1,5):
    for j in range (1, i+1):
        print(n, end = " ")
        n += 1
    print()



'''
NUMBER TRIANGLE
1
1 2 
1 2 3
1 2 3 4
'''
for i in range(1,5):
    for j in range(1,i+1):
        print(j, end = " ")
    print()


'''
REVERSE NUMBER TRIANGLE
1 2 3 4 
1 2 3
1 2
1
'''
for i in range(4,0,-1):
    for j in range(1, i+1):
        print(j, end = " ")
    print()



'''
ALPHABE TRIANGLE
A
A B
A B C
A B C D 
'''
for i in range(1,5):
    for j in range(1,i+1):
        print(chr(64+j), end = " ")
    print()



'''
ALPHABET - NUMBER TRIANGLE
1 2 3 4 5
1            1 
A B          2
1 2 3        3
A B C D      4
1 2 3 4 5    5
'''
for i in range(1,6):
    for j in range(1, i+1):
        if i%2==0 :
            print(chr(64 + j), end = " ")
        else:
            print(j, end=" ")
    print()



'''
0-1 TRIANGLE
1 2 3 4
1           1
0 1         2
1 0 1       3
0 1 0 1     4
'''
for i in range(1,5):
    for j in range(1,i+1):
        if (i+j) % 2 == 0:
            print("1", end = " ")
        else:
            print("0", end = " ")
    print()



'''
FLOYD's ODD NUMBER TRIANGLE
1 
3  5 
7  9  11 
13 15 17  19 
'''
c = 1
for i in range(1,5):
    for j in range(1,i+1):
        print(2*c-1, end = " ")
        c += 1
    print()



'''
ODD NUMBER TRIANGLE
1
1 3
1 3 5
1 3 5 7
'''
for i in range(1,5):
    for j in range (1, i+1):
        print( 2*j-1 , end = " ")            
    print()





  
