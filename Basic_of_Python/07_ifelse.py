# Single if statement
if 5 == 5:
    print("Both are equal")

if 5 < 10:
    print("10 is largest")


# if-else Statement

# Example - 1 : Print ODD or EVEN

# CASE 1 :
num = int(input("Enter a number:"))
if num % 2 == 0:
    print("EVEN")
else:
    print("ODD")

#CASE 2 : (using Bitwise operator)
number = int(input("Enter a number:"))
if number & 1:
    print("ODD")
else:
    print("EVEN")

# Explnation of CASE 2
#  it means -> number converted into Binary number and then add 1
'''
11 -> 00001011
1  -> 00000001
-----------------
& ->  00000001 --> last bit 1 then ODD num

6 -> 00000110
1 -> 00000001
-----------------
& ->  00000000 --> last bit 0 then EVEN num
'''



# if-elif statement 
# Example - 1 : Take 3 subject marks, Find percentage and give grade according percentage
eng = int(input("Enter marks of English:"))
math = int(input("Enter marks of Maths:"))
sci = int(input("Enter marks of Science:"))

per = ((eng + math + sci) * 100) / 300
print("Your percentages is:", per)

if per > 80:
    print("A Grade")
elif per > 65:
    print("B Grade")
elif per > 50:
    print("C Grade")
else:
    print("Fail!")



# Nested if-elif Statement
# Example - 1 : Print Positive odd/even or Negative odd/even

num = int(input("Enter a number:"))
if num > 0:
    if num & 1:
        print("Positive - ODD")
    else:
        print("Positive - EVEN") 
elif num < 0:
    if num & 1:
        print("Negative - ODD")
    else:
        print("Negative - EVEN")
else:
    print("Number is ZERO.")



# Use of LOGICAL Operators in if-elif

# Example - 1 : Find largest number using logical operator
n1 = int(input("Enter value of n1:"))
n2 = int(input("Enter value of n2:"))
n3 = int(input("Enter value of n3:"))

if n1 > n2 and n1 > n3:
    print("n1 is Lagest number:",n1)
elif n2 > n3:
    print("n2 is largest number:",n2)
else:
    print("n3 is largest number:",n3)


# Example - 2 : Check given Character is Alphabet or Number or Special Symbol
ch = input("Enter a Character:")

if (ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z'):
    print("ALPHABET")
elif (ch >= '0' and ch <= '9'):
    print("DIGIT")
else:
    print("SPECIAL SYMBOL")



# Example - 3 : Print that given character is vowel or consonant or digit or Special symbol
ch = input("Enter a Character:")

#if (ch == "A" or ch == "a" or ch == "E" or ch == "e" or ch == "I" or ch == "i" or ch == "O" or ch == "u" or ch == "U" or ch == "u"):
#   print("Vowel")

if ch in 'AEIOUaeoiu':
    print("Vowel")
elif (ch >= "A" and ch <= "Z") or (ch >= "a" and ch <= "z"):
    print("Consonent")
elif ch >= "0" and ch <= "9":
    print("Digit")
else:
    print("special symbol")

# Instead of the long if condition, We can write
# if ch in 'AEIOUaeiou':

