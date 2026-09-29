# We can change value of attributes
class Student:
    def __init__(self, name, age):
        self.name = name        # we can call it property 
        self.age = age

s1 = Student("Ram", 24)
print(s1.age)
s1.age = 26
print(s1.age)

# For delete the attribute use keyword - del
print(s1.name)
del s1.name
# print(s1.name) # AttributeError: 'Student' object has no attribute 'name'



# 2 types of attributes 
#   1. Class attribute  
#   2. Instance attribute

class Student:
    school = "XYZ School"   # Class attributes

    def __init__(self, name, age):
        self.name = name    # Instance attributes
        self.age = age


s1 = Student("Amit", 24)
s2 = Student("Sumita", 20)

print("Student 1 : ", s1.name, s1.age, s1.school)
print("Student 2 : ", s2.name, s2.age, s2.school)



# Update last name
class Person:
    lastname = ""

    def __init__(self, name):
        self.name = name


p1 = Person("Amit")
p2 = Person("Raj")
Person.lastname = "Pandey"

print(p1.name + " " + p1.lastname)
print(p2.name + " " + p2.lastname)




# Use a method in another method
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is " + self.name)

p1 = Person("Manan")
p1.greet()




# We can modify any attribute in another method also
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy birthday! You are now {self.age}")

p1 = Person("Ram", 25)
p1.celebrate_birthday()

print(p1)



