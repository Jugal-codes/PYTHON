# Assign function to variable
def greet():
    print("Hello")

x = greet
x()



# Pass function as argument
def greet():
    print("Namaste")

def call_func(func):
    func()

call_func(greet)



# Return function
def outer():
    def inner():
        print("Inner function")
    return inner

f = outer()
f()



# Store functions in list
def add(a, b): return a + b
def sub(a, b): return a - b

ops = [add, sub]
print(ops[0](12, 6))
print(ops[1](12, 6))
