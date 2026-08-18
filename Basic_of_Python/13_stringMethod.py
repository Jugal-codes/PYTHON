# String Methods

# 1. Case Conversion :

s1 = "hello World"
print(s1.upper()) #HELLO WORLD -> all letter in upper case
print(s1.lower()) #hello world -> all letter in lower case
print(s1.title()) #Hello World -> 1st letter of each word will capital
print(s1.capitalize()) #Hello world -> only 1st letter of string is capital
print(s1.swapcase()) #HELLO wORLD -> swap upper to lower nd lower to upper

print("--------------------------------------------------------------------------------")

# 2. Searching & Finding :

s2 = "Mississippi"

# find() -> find the substring nd print it's first found's starting index
#           if string isn't find then return -1
print(s2.find("i")) #1 -> at 1st index, nd give the index of first i
print(s2.find("i", 5)) #7 -> 'i' is substring nd 5 is start point -> find substring from 5 to length
print(s2.find("i", 5, 9)) #7 -> 5 is starting point nd 8 is ending point (9 isn't included)
print(s2.find("ss")) #2 -> substring also allowed not only character
print(s2.find("ssss")) #-1 -> not found then print -1
print("----------------------")

# rfind() -> find the substring nd print it's last found's starting index
#            if string isn't find then return -1
print(s2.rfind("i")) #10
print(s2.rfind("i", 1, 9)) #7 -> check 1 to 8 
print(s2.rfind("ss",1,8))   #5 -> check 1 to 7
print(s2.rfind("ssss")) #-1 -> not found so print -1
print("----------------------")

# index() ->  same work like find() but gives error if any string wasn't find out
print(s2.index("i")) #1 
print(s2.index("i", 4)) #4
print(s2.index("i", 5, 9)) #10
#print(s2.index("iii")) -> this will give error
print("----------------------")

# rindex() -> same work like rfind() but gives error if any string wasn't find out
print(s2.rindex("i")) #10
print(s2.rindex("i", 4)) #10
print(s2.rindex("i", 5, 9)) #7
#print(s2.rindex("iii")) -> this will give error
print("----------------------")

# count() -> count that how much time given string repeated
print(s2.count("i")) #4
print(s2.count("ss")) #2
print("----------------------")

#startswith() nd endswith() -> gives true or false value
print(s2.startswith("Mi")) #True
print(s2.startswith("mi")) #False
print(s2.startswith("i", 4, 8)) #True -> string start from 4 to 7 nd starts with letter 'i'

print(s2.endswith("pi")) #True
print(s2.endswith("pi", 5)) #True -> string ends with 'pi' which start from 5th index
print(s2.endswith("pi", 5, 9)) #False -> string starts from 5 to 8 nd ends with 'pi'

print("--------------------------------------------------------------------------------")

# 3. Modification & Replacement :

s3 = "   Hello   "
# strip() -> remove extra space from starting nd ending of the string
print(s3.strip()) #remove space from both side
print(s3.lstrip()) #remove space from left side only
print(s3.rstrip()) #remove space from right side only


s4 = "Mississippi"
# replace() -> replace the old string with new string 
print(s4.replace("i", "o"))
print(s4.replace("ss", "rr"))


print("--------------------------------------------------------------------------------")

# 4. Splitting & Joining :

s4 = "I am Python"
print(s4.split()) #split at space

s4 = "demo123@gmail.com"
print(s4.split("@")) #split at @

s4 = "a-b-c-d-e"
print(s4.split("-")) #split at -
print(s4.split("-", 2)) #split the first 2 - then gives rest of string in 1 element -> ['a', 'b', 'c-d-e']

# rsplit() -> reverse split function
print(s4.rsplit("-")) 
print(s4.rsplit("-", 2)) #split the last 2 - then gives rest of string in 1 element ->['a-b-c', 'd', 'e']

s4 = "a\nb\nc"
print(s4)
print(s4.split("\n"))
print(s4.splitlines()) # work like s4.split("\n")


li = ["a", "b", "c"]

# join list's element 
print(" ".join(li)) # a b c
print("-".join(li)) #a-b-c
print("$".join(li)) #a$b$c


# split() , rsplit() -> convert string to list element
# join() -> convert list element to string

print("--------------------------------------------------------------------------------")

# 5. Checking Content :


#isalnum() -> gives True for only numeric str, only alpabetic str nd mix string also
s = "abc123"
print(s.isalnum())  #True
s = "abc"
print(s.isalnum())  #True
s = "123"
print(s.isalnum())  #True
s = "!@#asd"
print(s.isalnum())  #False
print("----------------------")

#isalpha() -> gives True for only alphabetic string
s = "abc123"
print(s.isalpha())  #False
s = "123"
print(s.isalpha())  #False
s = "abc"
print(s.isalpha())  #True
print("----------------------")

#isdigit() -> gives True for only numeric string
s = "abc123"
print(s.isdigit())  #False
s = "123"
print(s.isdigit())  #True
s = "abc"
print(s.isdigit())  #False
print("----------------------")


s = "abc123"
print(s.isdecimal())    #False
s = "123"
print(s.isdecimal())    #True
s = "abc"
print(s.isdecimal())    #False
print("----------------------")

s = "¹" #exponent
print(s.isdigit()) #True
print(s.isdecimal()) #False
print("----------------------")

s = "⅔"
print(s.isnumeric())    #True
print("----------------------")

s = "var1"
print(s.isidentifier())     #True
s = "1var"
print(s.isidentifier())     #False
s = "var_1"
print(s.isidentifier())     #True
s = "var()"
print(s.isidentifier())     #False
s = "_"
print(s.isidentifier())     #True
print("----------------------")

s = "    "
print(s.isspace())      #True
s = " 4   "
print(s.isspace())      #False
print("----------------------")

print("hello".isupper())
print("hello".islower())
print("HELLO".isupper())
print("HELLO".islower())
print("hello World".istitle())
print("Hello world".istitle())
print("Hello World".istitle())




