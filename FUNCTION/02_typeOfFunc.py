'''
Types of Function :    
    1.Built-in Function     2.User-defined Function

Types of Built-in Function:
    1. any()        2. all()        3. sorted()

Types of User-Defined Function:
    1. No Return Type No Arguments          2. No Return Type With Arguments
    3. With Return Type No Arguments        4. With Return Type With Arguments
'''

# Built-in Function

# any() function --> if any 1 true - gives True
nums = [False, False, True, False]
print(any(nums)) #True

nums = [False, False, False, False]
print(any(nums)) #False

nums = [0, 0, 0, 5]
print(any(nums)) #True

marks = [25, 30, 35, 80]
result = any(mark >= 40 for mark in marks)
print(result) #True

tuple = (0, 0, 0, 1)
print(any(tuple)) #True

set = {0, 1}
print(any(set)) #True

# REMEMBER IT 
dict = {"rohit": 90, "manan": 0, "raj": 10}
print(any(v >= 95 for k, v in dict.items())) #False


print("------------------------------------------------------")


# all() function --> if all true - gives True otherwise False
nums = [True, True, True]
print(all(nums)) #True

nums = [True, False, True]
print(all(nums)) #False

nums = [10, 20, 30]
print(all(nums)) #True

marks = [50, 60, 70, 80]
result = all(mark >= 40 for mark in marks)
print(result) #True

marks = [50, 60, 20, 80]
print(all(mark >= 40 for mark in marks)) #False


print("------------------------------------------------------")


# sorted() function --> 3 parameter - iteration, key=None, reverse=False
nums = [50, 10, 30, 20]
print(sorted(nums)) #[10, 20, 30, 50]

nums = [50, 10, 30, 20]
print(sorted(nums, reverse=True)) #[50, 30, 20, 10]

names = ["Raj", "Amit", "Kiran"]
print(sorted(names)) #['Amit', 'Kiran', 'Raj']

data = (5, 2, 8, 1)
print(sorted(data)) #[1, 2, 5, 8]

names = ["Python", "C", "Java", "JavaScript"]
print(sorted(names, key=len)) #['C', 'Java', 'Python', 'JavaScript']

# we can use lambda fun in key
words = ["cat", "apple", "dog", "banana"]
print(sorted(words, key=lambda x: x[-1])) #['banana', 'apple', 'dog', 'cat']

# abs => |-10| = 10
nums = [-10, 5, -2, 8]
print(sorted(nums, key=abs)) #[-2, 5, 8, -10]

# In dict
student = {"name": "Raj", "age": 20, "city": "Ahmedabad"}
print(sorted(student)) #['age', 'city', 'name'] -> sorted by key

# In object
people = [
    {"name": "Raj", "age": 25},
    {"name": "Amit", "age": 20},
    {"name": "Kiran", "age": 30},
]
result = sorted(people, key=lambda x: x["age"], reverse=True)
print(result) #[{'name': 'Kiran', 'age': 30}, {'name': 'Raj', 'age': 25}, {'name': 'Amit', 'age': 20}]

students = [("Raj", 80), ("Amit", 60), ("Kiran", 90)]
print(sorted(students, key=lambda x: x[1])) #[('Amit', 60), ('Raj', 80), ('Kiran', 90)]




# User-defined Function

# 1. No Return Type No Arguments
def wish():
    print("Good Evening!")

wish()
wish()

# 2. No Return Type With Arguments
def sum(a, b):
    print(f"{a} + {b} = {a+b}")

sum(34,67)

# 3. With Return Type No Arguments
def mul():
    a = int(input("Enter value of a:"))
    b = int(input("Enter value of b:"))

    return a*b

# mul() //do not print value 
multip = mul()
print(multip)

# 4. With Return Type With Arguments
def Grade(m1, m2, m3, m4, m5):
    total = m1 + m2 + m3 + m4 + m5
    per = total * 100 / 500
    print(f"Total marks:{total} and Percentage:{per}%")

    if per >= 80:
        return "A"
    elif per >= 65:
        return "B"
    elif per >= 50:
        return "C"
    elif per >= 35:
        return "D"
    else:
        return "FAIL"

marks = Grade(98, 8, 29, 2, 8)
print(marks)
