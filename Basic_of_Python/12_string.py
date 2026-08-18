# We can write string in 3 way -> ' ' , " " , """ """ , ''' '''
# String - immutable
str1 = "Hello"
str2 = 'bye'
str3 = """HELLO"""
str4 = '''Bye'''
print(str1)
print(str2)
print(str3)


# String Indexing
'''
    H   E   L   L   O
    0   1   2   3   4
   -5  -4  -3  -2  -1
'''
s1 = "HELLO"
print(s1[2])
print(s1[0])
print(s1[-1])
print(s1[-2])


# String Slicing [start:end:step]
'''
    M       i       s       s       i       s       s       i       p       p       i
    0       1       2       3       4       5       6       7       8       9       10
   -11     -10     -9      -8      -7      -6      -5      -4      -3      -2      -1
'''
s2 = "Mississippi"
print(s2[0:5]) #Missi -> 5th index excluded
print(s2[4:9]) #issip -> 9th index excluded
print(s2[:7])  #start from 0th & end at 6th index
print(s2[3:])  #start from 3rd & end at last index
print(s2[:])   #print whole string
print(s2[0:9:2]) # 0 to 8, nd skip 1 letter
print(s2[0:9:4]) # 0 to 8, nd skip 3 letters
print(s2[-4:-9]) #Empty string bcz (-4)>(-9) nd index work left to right
print(s2[-9:-4]) #-4th index are not included -> ssiss
print(s2[::-1]) #Print reverse string
print(s2[1:7:-1]) #Empty string bcz 1<7 bt here step is (-1) which flow is right to left
print(s2[7:1:-1]) #ississ ->  1st index aren't included
print(s2[-4:-9:-1]) #sissi -> -9th index aren't included
print(s2[-4:-9:-3]) #-4 to -8, nd skip 2 letters 
print(s2[2:-3]) #2 to (total len + (-3)) -> 2 to 7 -> ssissi



