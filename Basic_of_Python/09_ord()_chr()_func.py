# ord() nd chr() function ==> MOST IMPORTANT TOPIC

# ord() convert Character to it's Number
# chr() convert Number to it's Character

# ord() function : 
x = ord("A")
print(x)        #65

x = ord("*")
print(x)        #42

x = ord("😊")
print(x)        #128522

# x = ord("Hello")
# print(x)        #Error


# chr() convert Number to it's Character
x = chr(65)
print(x)        #A

x = chr(42)
print(x)        #*

x = chr(128522)
print(x)        #😊



# TASK - 1 : Convert capital alphabet to small & small to capital

# A -> a and b -> B

ch = input("Enter a character:")

if ch >= 'A' and ch <= 'Z':
    ch = chr(ord(ch) + 32)
elif ch >= 'a' and ch <= 'z':
    ch = chr(ord(ch) - 32)

print(ch)
