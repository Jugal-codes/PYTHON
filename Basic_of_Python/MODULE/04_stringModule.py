'''
String module provides 
    predefined string constants and some helpful utilities to work with text easily.

It mainly contains:
    Alphabets, Digits, Special characters, Whitespace characters
'''

import string as s

# 1. string.ascii_letters : All uppercase + lowercase letters
print(s.ascii_letters)

# 2. string.ascii_lowercase : All lowercase letters
print(s.ascii_lowercase)

# 3. string.ascii_uppercase : All uppercase letters
print(s.ascii_uppercase)

# 4. string.digits : Digits from 0 to 9
print(s.digits)

# 5. string.hexdigits : Hexadecimal digits 
print(s.hexdigits)

# 6. string.octdigits : Octal digits (0–7)
print(s.octdigits)

# 7. string.punctuation : All special characters
print(s.punctuation)

# 8. string.whitespace : Space, tab, newline, etc.
print(s.whitespace)





# TASK - 1 -> Count digits in a string :
import string as s

str = input("Enter a string: ")
count = 0

for ch in str:
    if ch in s.digits:
        count += 1

print("Total digits:", count)



# TASK - 2 -> Count alphabets in a string :
import string as s

str = input("Enter a string: ")
count = 0

for ch in str:
    if ch in s.ascii_letters:
        count += 1

print("Total letters:", count)



# TASK - 3 -> Random Password Generator :
import random as r
import string as s

chars = s.ascii_letters + s.digits
password = ""

for i in range(6):
    password += r.choice(chars)

print("Password:", password)