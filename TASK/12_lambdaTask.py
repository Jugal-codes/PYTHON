"""
# PRACTICE TASK --> map function with lambda
1. Create a list of numbers and use map() to find squares of all numbers.
2. Create a list of numbers and use map() to convert all numbers into strings.
3. Given a list of temperatures in Celsius, use map() to convert them into Fahrenheit.
4. Create a list of names and use map() to convert all names into uppercase.
5. Given a list of strings, use map() to find the length of each string.
6. Create a list of numbers and use map() to add 10 to every element.
7. Given a list of words, use map() to reverse each word.
8. Create a list of prices and use map() to add 18% GST to every price.
9. Create a list of integers and use map() to check whether each number is even or odd.
"""

# 1. Create a list of numbers and use map() to find squares of all numbers.
li = [1, 2, 3, 4, 5]

square = list(map(lambda n: n ** 2, li))
print(square)


# 2. Create a list of numbers and use map() to convert all numbers into strings.
li = [1, 2, 3, 4, 5]

string = list(map(lambda n: str(n), li))
print(string)


# 3. Given a list of temperatures in Celsius, use map() to convert them into Fahrenheit.
li = [0, 25, 37, 30, 100]

fah = list(map(lambda n: ((n* 9/5) + 32), li))
print(fah)


# 4. Create a list of names and use map() to convert all names into uppercase.
li = ["Amit", "Sumit", "Ram", "Shyam"]

cap = list(map(lambda name: name.upper(), li))
print(cap)

# 5. Given a list of strings, use map() to find the length of each string.
li = ["Amit", "Sumit", "Ram", "Shyam"]

length = list(map(lambda name: len(name), li))
print(length)


# 6. Create a list of numbers and use map() to add 10 to every element.
li = [1, 2, 3, 4, 5]

plus = list(map(lambda n: n+10, li))
print(plus)

# 7. Given a list of words, use map() to reverse each word.
li = ["amit", "sumit", "ram", "shyam"]

rev = list(map(lambda name: name[::-1], li))
print(rev)

# 8. Create a list of prices and use map() to add 18% GST to every price.
price = [220, 500, 100, 456, 789]

gst = list(map(lambda p: (p*18)/100, price))
print(gst)

# 9. Create a list of integers and use map() to check whether each number is even or odd.
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

check = list(map(lambda n: "Even" if n%2==0 else "Odd", li))
print(check)


 
"""
# PRACTICE TASK --> filter function with lambda
1. Filter Even Numbers => numbers = [1, 2, 3, 4, 5, 6, 7, 8]
2. Filter Odd Numbers => numbers = [1, 2, 3, 4, 5, 6, 7, 8]
3. Filter Positive Numbers => numbers = [-5, 10, -2, 8, 0]
4. Filter Names Starting With A => names = ["Akshay", "Rahul", "Amit", "Karan"]
5. Filter Strings With Length More Than 5 => words = ["apple", "banana", "kiwi", "mango"]
6. Filter Vowels From List => letters = ['a', 'b', 'e', 'f', 'i']
7. Filter Palindrome Words => words = ["madam", "python", "level", "code"]
8. Filter Uppercase Words => words = ["HELLO", "Python", "WORLD", "Code"]
9. Filter Alphabet Characters => data = ['A', '1', 'B', '9', 'C']
10. Filter Strings Containing Letter "a" => words = ["apple", "mango", "berry", "banana"]
"""


# 1. Filter Even Numbers
num = [1, 2, 3, 4, 5, 6, 7, 8]

even = list(filter(lambda n: n%2==0, num))
print(even)


# 2. Filter Odd Numbers
num = [1, 2, 3, 4, 5, 6, 7, 8]

odd = list(filter(lambda n: n%2!=0, num))
print(odd)


# 3. Filter Positive Numbers
num = [-5, 10, -2, 8, 0]

positive = list(filter(lambda n: n>0, num))
print(positive)


# 4. Filter Names Starting With A
names = ["Akshay", "Rahul", "Amit", "Karan"]

withA = list(filter(lambda name: name.startswith("A"), names))
print(withA)


# 5. Filter Strings With Length More Than 5
word = ["apple", "banana", "kiwi", "mango"]

# new = list(filter(lambda w: len(w)>=5, word))
new = list(filter(lambda w: len(w)>5, word))
print(new)


# 6. Filter Vowels From List
letter = ['a', 'b', 'e', 'f', 'i', 'A', 'D', 'U']

vowel = list(filter(lambda l: l in 'aeiouAEIOU', letter ))
print(vowel)


# 7. Filter Palindrome Words
word = ["madam", "python", "level", "code"]

pal = list(filter(lambda w: w == w[::-1], word))
print(pal)


# 8. Filter Uppercase Words
word = ["HELLO", "Python", "WORLD", "Code"]

new = list(filter(lambda w: w == w.upper(), word))
print(new)


# 9. Filter Alphabet Characters
data = ['A', '1', 'B', '9', 'C']

new = list(filter(lambda d: d.isalpha(), data))
print(new)


# 10. Filter Strings Containing Letter "a"
words = ["apple", "mango", "berry", "banana", "kiwi"]

fil = list(filter(lambda w: "a" in w, words))
print(fil)




"""
# PRACTICE TASK --> reduce function with lambda 
1. Concatenate Strings => words = ["Python", "is", "awesome"]
2. Reverse a String => word = "python"
3. Find Total Digits in List => numbers = [123, 45, 6789]
4. Find Highest Marks => marks = [45, 78, 90, 66, 88]
5. Count Total Words Length => words = ["python", "java", "c"]
"""


from functools import reduce

# 1. Concatenate Strings
words = ["Python", "is", "awesome"]

str = reduce(lambda a,b: a + b, words)
print(str)


# 2. Reverse a String
word = "python"

rev = reduce(lambda a,b: b + a, word)
print(rev)


# 3. Find Total Digits in List
num = [123, 45, 6789]

total_digits = reduce(lambda x, y: x + len(str(y)), num, 0)
print(total_digits)
# OR
t = reduce(lambda a,b: str(a) + str(b), num)
print(len(t))
# OR
t1 = reduce(lambda a,b: a + len(str(b)), num, 0)
print(t1)



# 4. Find Highest Marks
marks = [45, 78, 90, 66, 88]

max = reduce(lambda a,b : a if a>b else b, marks)
print(max)


# 5. Count Total Words Length
words = ["python", "java", "c"]
print(len(words))

leng = reduce(lambda a, b : a + b, words)
print(len(leng))



"""
# PRACTICE TASK -> Use map, filter, reduce func for one task
1. Square Even Numbers and Find Sum
2. Sum of Cubes of Positive Numbers
3. Find Sum of Squares of Odd Numbers
4. Find Largest Square of Even Numbers
5. Reverse Long Words and Join Filter words whose length is greater than 4.
"""

# 1. Square Even Numbers and Find Sum
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# square = list(map(lambda n: n**2, num))
# print(square)
# even = list(filter(lambda n: n%2==0, num))
# print(even)

from functools import reduce

sum = reduce(
    lambda a,b: a+b, 
    list(map(lambda n: n**2, list(filter(lambda n: n%2==0, num)))))
print(sum)


# 2. Sum of Cubes of Positive Numbers
num = [1, 0, 3, -4, 5, 6, -7, 8, 9, -10]

# cube = list(map(lambda n: n**3, num))
# print(cube)
# positive = list(filter(lambda n: n>0, num))
# print(positive)

from functools import reduce

sum = reduce(
    lambda a,b : a+b, 
    list(map(lambda n: n**3, list(filter(lambda n: n>0, num)))))
print(sum)


# 3. Find Sum of Squares of Odd Numbers
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# square = list(map(lambda n: n**2, num))
# print(square)
# odd = list(filter(lambda n: n%2!=0, num))
# print(odd)

from functools import reduce

sum = reduce(
    lambda a,b: a+b, 
    list(map(lambda n: n**2, list(filter(lambda n: n%2!=0, num)))))
print(sum)


# 4. Find Largest Square of Even Numbers
num = [1, 2, 3, 10, 5, 6, 7, 8, 9, 12]

# square = list(map(lambda n: n**2, num))
# print(square)
# even = list(filter(lambda n: n%2==0, num))
# print(even)

from functools import reduce

max = reduce(
    lambda a,b : a if a>b else b, 
    list(map(lambda n: n**2, list(filter(lambda n: n%2==0, num)))))
print(max)


# 5. Reverse Long Words and Join Filter words whose length is greater than 4.
# reverse all words, then filter len > 4,  then join all that words
word = ['apple', 'kiwi', 'banana', 'orange', 'lichi', 'pear']

# rev = list(map(lambda w: w[::-1], word))
# print(rev)
# leng = list(filter(lambda w: len(w)>4, word))
# print(leng)

from functools import reduce

result = reduce(
    lambda a,b : a + b, 
    list(map(lambda w: w[::-1], list(filter(lambda w: len(w)>4, word)))))
print(result)


