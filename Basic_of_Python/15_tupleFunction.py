# Tuple Operation

# 1. Concatenation
t1 = (1, 2, 30)
t2 = (4, 5, 6)
concate = t1 + t2
print(concate) #(1, 2, 30, 4, 5, 6)


# 2. Repetition
print(t1 * 3) #(1, 2, 30, 1, 2, 30, 1, 2, 30)


# 3. Membership  
print(1 in t1) #True
print(11 in t1) #False
print(1 not in t1) #False
print(11 not in t1) #True

print("---------------------------")

# Tuple Function
print(len(t1)) #3
print(max(t1)) #30
print(min(t1)) #1
print(sum(t1)) #33

# tuple() - for type casting
li = [1, 2, 3, 4, 5]
t = tuple(li)
print(t) #(1, 2, 3, 4, 5)

# count() - count 'ch' in string
# index() - find 1st occurence of 'ch'
s = "Hello"
t = tuple(s)
print(t) #('H', 'e', 'l', 'l', 'o')

print(t.count("l")) #2
print(t.index("l")) #2


# Tuple Packing & Unpacking
t = 1, "Ram", 8.5, 1, 2, 3, 4, 5
print(t) #(1, 'Ram', 8.5, 1, 2, 3, 4, 5)

roll, name, marks, *other = t
print(roll) #1
print(name) #Ram
print(marks) #8.5
print(other) #[1, 2, 3, 4, 5]