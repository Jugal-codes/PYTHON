# Arbitrary arguments -> *args & **kargs


# *args -> Arbitrary Positional Arguments
# It’s used when you want a function to accept any number of positional arguments.
def demo(a, b, *args):
    print(a) #10
    print(b) #20
    print(args) #(30, 40, 50)
    # for sum
    total = a + b + sum(args)
    return total

demo(10, 20, 30, 40, 50)


def printLi(*args):
    print(args) #(1, 2, 3, 4, 5)

printLi(*[1, 2, 3, 4, 5])
li = [1, 2, 3, 4, 5]



# **kargs -> Arbitrary Keyword Arguments
# It’s used when you want a function to accept any number of keyword arguments.
person = {"Name": "Ram", "Age": 21, "City": "Ahm"}
def printDict(**kargs):
    print(kargs) #{'Name': 'Ram', 'Age': 21, 'City': 'Ahm'}

printDict(**person)



# Using Both Together
def demo(a, b, *args, **kwargs):
    print("a:", a) #a: 10
    print("b:", b) #b: 20
    print("args:", args)        # tuple - args: (30, 40)
    print("kwargs:", kwargs)    # dictionary - kwargs: {'x': 100, 'y': 200}

demo(10, 20, 30, 40, x=100, y=200)
