# TASK - 1
# Create a class "Programmer" for storing information of few programmers working at Microsoft.
class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

        print(f"Developer {self.name} is from {self.pin} which salary are {self.salary} at {self.company} ")

p1 = Programmer("Amit", 120000, 380001)
p2 = Programmer("Sumit", 150000, 380008)


# TASK - 2
# Write a class "Calculator" capable of finding square, cube and square root of a number.
class Calculator:
    def __init__(self, num):
        self.num = num
        print(f"Square:{self.num*self.num}\nCube:{self.num*self.num*self.num}\nSquare root:{self.num**1/2}")
        
c1= Calculator(4)


# TASK - 3
# Create a class with a class attribute a; create an object from it and set 'a' directly using object.
# a = o. Does this change the class attribute?      (Ans. - NO)
class Change():
    a = 5

o = Change()
print(o.a)  # Print the class attribute bc instance attribute isn't present
o.a = 123   # Instance attribute is set
print(o.a)
print(Change.a) # class attribute isn't changed 



# TASK - 4 
# Add static method in task-2, to greet the user with hello
class Calculator:
    def __init__(self, num):
        self.num = num
        print(f"Square:{self.num*self.num}\nCube:{self.num*self.num*self.num}\nSquare root:{self.num**1/2}")

    @staticmethod
    def greet():
        print("End of calculator!")

c1= Calculator(4)
c1.greet()


# TASK - 5
# Write a class train which has method book a ticket, get status (no of seats) and 
# get fare information of train running under Indian Railways.
from random import randint
class Train():
    def __init__(self, trainNo, fro, to):
        self.trainNo = trainNo
        self.fro = fro
        self.to = to

    def bookTicket(self):
        print(f"Ticket is booked in train no {self.trainNo} from {self.fro} to {self.to}.")

    def getStatus(self):
        print(f"Train no {self.trainNo} is running on time..")

    def getFare(self):
        print(f"Train fare for train no {self.trainNo} from {self.fro} to {self.to} is {randint(100,500)}.") 
        
t1 = Train(1489, "AHMEDABAD", "DWARKA")
t1.bookTicket()
t1.getStatus()
t1.getFare()



# TASK - 6
# Can you change the self-parameter inside a class to something else (say "python").
# Try changing self to "slf" or "python" and see the effects.

# ANSWER : yes, we can but it isn't a good practice...