# Now, we try to write if-else condition in one line

# For if-else statement

# Example - 1 : Find Bigger number
# With multiple line
x = 10
y = 20
if x > y:
    print("X is Bigger")
else:
    print("Y is bigger")


# In a single line
x = 10
y = 20
result = "X is Bigger" if x>y else "Y is bigger"
print(result)
#                  ' OR '
print("X is Bigger") if x>y else print("Y is bigger")



# Example - 2 : Distribute Grade according percentage 
# With multiple line
per = 89

if per >= 90:
    print("A")
elif per >= 80:
    print("B")
elif per >= 70:
    print("C")
elif per >= 60:
    print("D")
elif per >= 50:
    print("E")
else:
    print("Fail")

# In a single line
per = 55
print("A Grade") if per>=80 else print("B Grade") if per>=65 else print("C Grade") if per>=50 else print("FAIL")



