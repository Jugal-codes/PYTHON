class Employee:
    company = "Google"

    # Using no attributes
    def hello(self):
        print("Hello to All!")

    # Using instance attribute
    def greet(self):   
        print(f"Good Morning, {self.name}!")

    # Using class attribute
    def greet1(self):
        print(f"Welcome to {self.company}!")
    
emp = Employee()
emp.name = "Jugal"
emp.hello()
emp.greet()
emp.greet1()

# 'self' parameter mostly used in methods.
# You can use anyword insted of 'self' like a, ul, sl etc.


# def hello(self):
#   print("Hello to All!")
# For this type of method use @staticmethod

class Static:
    @staticmethod   
    def hello():
        print("Hello Users!")

s1 = Static()
s1.hello()



# __init__() method which is called dunder method also
class Employee:
    def __init__(self):
        print("This is an automatically called..")
    def greet(self):
        print(f"Hello, {self.name}!")

emp = Employee()
emp.name = "Jugal"
emp.greet()


# Default value - put that parameter at end
class Programmer:
    company = "Microsoft"

    def __init__(self, name, pin, salary = 12000):
        self.name = name
        self.salary = salary
        self.pin = pin

        print(f"Developer {self.name} is from {self.pin} which salary are {self.salary} at {self.company} ")

p1 = Programmer("Amit", 380001)
p2 = Programmer("Sumit", 380008)

