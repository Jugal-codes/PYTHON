# Syntax : lambda arguments : expression

# Normal way
def add(a, b):
    return a + b
print(add(3, 4))

# Using lambda
add2 = lambda a,b : a+b
print(add2(20,40))



# Even - Odd
def evenodd(num):
    if num%2==0:
        return "EVEN"
    else:
        return "ODD"

print(evenodd(100))

# Using lambda
evenodd2 = lambda num : "Even" if num%2==0 else "Odd"
print(evenodd2(99))



# Positive - Negative - using if else
type = lambda n: "Positive" if n > 0 else "Negative" if n < 0 else "Zero"

print(type(10))
print(type(-55))
print(type(0))



# Login system 
login = lambda user, pwd: (
    "Admin Login" if user == "admin" and pwd == "007" else
    "User Login" if user == "user" and pwd == "xyz" else
    "Invalid Login"
)

print(login("admin", "123"))
print(login("user", "xyz"))
print(login("admin", "007"))



