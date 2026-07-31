# Normal print statement
print("Good Morning")

# If we write 2 print statement then 2nd take new line
print("Good")
print("Morning")

# OR we can use  \n -> new line character
print("Good\nMorning")

# We can also use \t -> tab character
print("Good\tMorning")  

# We can also use \b -> backspace character
print("Good\b Morning")  #Goo Morning
print("Good\b\b Morning")  #Go Morning



#`Good"
print("`Good\"")
# after \ fist char or symbol will be consider as string part

# Good\
print("Good\\")


#Ocatal number - consider with \ and 0 to 7
print("\103") #C

#Hexadecimal number - consider with \x and 0 to 9 and A to F
print("\x41") #A


# How to scane the input from user

# For string input
name = input("Enter your name: ")
print("Hello", name)

# For integer input
age = int(input("Enter your age: "))    
print("Your age is", age)

# For float input
height = float(input("Enter your height in meters: "))  
print("Your height is", height, "meters")



# Multi line comment in python can be done using triple quotes (''' ''' or """ """).
"""
qwertyhj
aswedrfgh
sdf
"""


# Indentation is important in python, it is used to define the scope of loops, functions, and classes.
# In python, we use indentation to indicate a block of code.
if 5 < 2 : 
    print("5 is greater than 2") #5 is greater than 2
else :
    print("5 is not greater than 2")



