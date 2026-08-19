# 3 type of operation : Set Operations , Comparison Operation , Update Operation 

# 1. Set Operation - Union(|) , Intersection(&) , Difference(-) , Symmetric Difference(^)
# Two way to write operation

a = {1, 2, 3}
b = {3, 4, 5}

# Union
print(a | b)  # {1, 2, 3, 4, 5}
print(a.union(b))

# Intersection
print(a & b)  # {3}
print(a.intersection(b)) 

# Difference
print(a - b)  # {1, 2}
print(a.difference(b))

print(b - a)  # {1, 2}
print(b.difference(a))

# Symmetric Difference
print(a ^ b)  # {1, 2, 4, 5}
print(a.symmetric_difference(b))






# 2. Set Comparison Operations - subset , superset, disjoint set

a = {1, 2}
b = {1, 2, 3}

# Subset
print(a <= b)  # True
print(a.issubset(b))  # True

# Superset
print(b >= a)  # True
print(b.issuperset(a))  # True

# Disjoint set
x = {1, 2}
y = {3, 4}
print(x.isdisjoint(y))  # True -> no common element





# 3. Update Operations (Modify Original Set) - 
#       Update (Union Update), Intersection Update, Difference Update, Symmetric Difference Update, Frozen Set

# Update (Union Update)
a = {1, 2}
b = {3, 4}

a.update(b)
print(a) #{1, 2, 3, 4}
print(b) #{3, 4}


# Intersection Update
a = {1, 2, 3}
b = {2, 3, 4}

a.intersection_update(b)
print(a)  # {2, 3}


# Difference Update
a = {1, 2, 3}
b = {2}

a.difference_update(b)
print(a)  # {1, 3}


# Symmetric Difference Update
a = {1, 2, 3}
b = {3, 4}

a.symmetric_difference_update(b)
print(a)  # {1, 2, 4}


# Frozen Set - Immutable set
fs = frozenset([1, 2, 3])
# fs.add(4)  # Error (immutable)

