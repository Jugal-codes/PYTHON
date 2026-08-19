# Different way to write a tuple
t1 = (1, 2, 3, 4)
print(t1) #(1, 2, 3, 4)

t2 = (10, "Ram", 8.5, True)
print(t2) #(10, 'Ram', 8.5, True)

t3 = 1, 2, 3, 4
print(t3) #(1, 2, 3, 4)
print(type(t3)) #<class 'tuple'>

# Tuple with 1 element
t4 = (10,)
print(t4) #(10,)
print(type(t4)) #<class 'tuple'>

t5 = (10)
print(t5) #10
print(type(t5)) #<class 'int'>

# Empty Tuple
t6 = ()
print(t6) #()
print(type(t6)) #<class 'tuple'>
print(len(t6)) #0

print("------------------------------------")

t = (10, 20, 30, 40, 50)

# Accessing elements
print(t[0]) #10 - First element
print(t[-1]) #50 - Last element
print(t[-3]) #30

# Slicing tuple
print(t[1:4]) #(20, 30, 40) - From index 1 to 3
print(t[:3]) #(10, 20, 30) - First 3 elements
print(t[-3:]) #(30, 40, 50) - Last 3 elements


