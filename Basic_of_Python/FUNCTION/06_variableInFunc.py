# Global & Local Variable

# 1.Local Variable
# A variable declared inside a function is local to that function.
# It only exists while the function is running.
# You cannot access it outside the function.

def demo():
    x = 100   # local variable
    print(x)

demo()
# print(x)   #Error: x is not defined outside


# 2. Global Variable
# A variable declared outside all functions is global.
# It can be accessed inside functions, but if you want to modify it, you must use the global keyword.

y = 200
z = 200

def Demo():
    x = 10    # Local variable
    global y, z    # tell Python we want to use global y and z
    y += 200  # y = y + 200
    z = z + 100

    print(x)   # local
    print(y)   # modified global
    print(z)   # modified global

Demo()
# print(x)    #Error
print(y)   # global y after modification




x = 2000   # Global variable
def demo():
    x = 100   # Local variable (inside function)
    print(x)  # Prints local x

demo()
print(x)      # Prints global x
