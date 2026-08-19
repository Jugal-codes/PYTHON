# Practice Qs - 1 : Count Characters
# Input a string and count the total number of characters without using len().

str = input("Enter a string:")
count = 0

for i in str:
    # print(i)
    count += 1
print(f"Character Count: {count}")


# Practice Qs - 2 : Count Vowels and Consonants
# Find the number of vowels and consonants in a string.

#str2 = "Mississippi"
str2 = input("Enter a string:")
vowC = 0
conC = 0

for i in str2:
    if i in 'AEIOUaeiou':
        vowC += 1
    else:
        conC += 1

print("Vowel Count:", vowC)
print("Consonant Count:", conC)



# Practice Qs - 3 : Reverse a String
# Reverse a given string without using slicing ([::-1]).
'''
example :   Doremon
            nomeroD
D   o   r   e   m   o   n
0   1   2   3   4   5   6
'''

s = input("Enter a name : ")
rev = ""

for i in range(len(s) - 1, -1, -1):
    rev = rev + s[i]

print("Reverse :", rev)



# Practice Qs - 4 : Check Palindrome
# Check whether a string is a palindrome or not.

s = input("Enter a name : ")
rev = ""

for i in range(len(s) - 1, -1, -1):
    rev = rev + s[i]

print("Reverse :", rev)

if s == rev:
    print("Palindrome String")
else:
    print("Not Palindrome String")


# Practice Qs - 5 : Count Words
# Count the number of words in a sentence.

str5 = input("Enter a sentence:") #"I am python developer."

newS = str5.split(" ")
print("Total number of words:",len(newS))


# Practice Qs - 6 : Convert Case
# Convert all lowercase letters to uppercase and vice versa.
# 'A' -> 'a'    and     'a' -> 'A'

str6 = "AAbbCCdd"
print(str6)

new = ""
for i in str6:
    if i >= 'A' and i <= 'Z':
        new = new + i.lower()
    elif i >= 'a' and i<='z':
        new = new + i.upper()
print(new)



# Practice Qs - 7 : Remove Spaces
# Remove all spaces from a string.
# ex : i am python developer
# output : iampythondeveloper


# CASE 1:
s = input("Enter a string : ")
output = ""
for i in s:
    if i != " ":
        output += i
print("Output :", output)


# CASE 2:
s = input("Enter a string : ")
print("Replace :", s.replace(" ", ""))



# Practice Qs - 8 : Find Frequency of a Character
# Count how many times a given character appears in a string.
# s2 = "Mississippi"
# ch = i -> 4 times

s = input("Enter a string : ")
ch = input("Enter a character you want to count : ")
cc = 0

for i in s:
    if i == ch:
        cc += 1
print(f"{ch} occurs {cc} times")




# Practice Qs - 9 : Replace a Word
# Replace all occurrences of a word with another word.
'''
Example => s2 = "Mississippi"
old = 'i'
new = 'o'
'''

# CASE - 1 :
s2 = "Mississippi"

new_str = s2.replace("i","o")
print(new_str)


# CASE - 2 :
s = input("Enter a string : ")
old = input("Enter Repalce character or word: ")
new = input("Enter new character or word : ")

new_s = ""

for i in s:
    if i == old:
        new_s += new
    else:
        new_s += i

print("Old String :", s)
print("New String :", new_s)



# Practice Qs - 10 : Find Longest Word
# Find the longest word in a sentence.
# example : i am python developer
# longest word : developer

s = input("Enter a string : ")
li = s.split()

print(li)

longest = li[0]

for i in li:
    if len(i) > len(longest):
        longest = i

print("Longest :", longest)

