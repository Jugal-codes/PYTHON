# Built-in Function TASK

# 1. Sort List of Dictionaries by Name
employees = [
    {"name": "Raj", "salary": 40000},
    {"name": "Amit", "salary": 50000},
    {"name": "Kiran", "salary": 35000},
    {"name": "Bhavna", "salary": 45000}
]
result = sorted(employees, key=lambda n: n["name"])
print(result)


# 2. Sort Strings by Number of Vowels
words = ["education", "apple", "python", "india", "computer"]

s = sorted(words, key=lambda word: sum(1 for ch in word.lower() if ch in "aeiou"))
print(s)


# 3. Sort Numbers by Last Digit
num = [42, 35, 17, 28, 63, 91]

result = sorted(num, key = lambda n: n%10)
print(result)



# User-defined Function TASK

# 1. Print String in function
def printChar(s):
    for i in s:
        print(i)

printChar("Doremon")


# reversed string
def reverseStr(s):
    return s[::-1]

print("Reverse String:",reverseStr("Doremon"))



# 2. Print list in function (Dict, Tuple, Set)
def printList(l):
    for i in l:
        print(i)

li = [1, 2, 3, 4, 5]
printList(li)



# 3. Print Square List
def squareList(l):
    sl = []
    for i in l:
        sl.append(i * i)
    return sl

x = squareList([1, 2, 3, 4, 5])
print(x)



# 4. Give multiple value in return
def math(a,b):
    return a+b, a-b, a*b, a/b

x = math(20, 10)
print(x)
print(type(x))



# 5. Factorial Function
def fact():
    n = int(input("Enter value of a:"))
    fact = 1

    for i in range(1, n+1):
        fact *= i
    print(f"Factorial of {n} is {fact}")

fact()



# 6. Find Prime Num
def prime(n):
    count = 0
    for i in range(1,n+1):
        fact = 0
        for j in range (1,i+1):
            if i%j == 0:
                fact += 1
        if fact == 2:
            print(i)
            count += 1
    print("Count : ", count)

prime(10)



# 7. Default value nd Positional Value
def add(a, b=20, c=30):
    print(f"{a} + {b} + {c} = {a+b+c}")

add(30, 40, 50)
add(10)
add(b=4, c=2, a=10)