#  Creating Set 
# 1st Approach : using {} 
s1 = {1, 2, 3, 4, 5, 5}
print(s1) #{1, 2, 3, 4, 5} - don't allow duplicates

# 2nd Approach : using set() functtion
s2 = set([1, 1, 3, 2, 5, 4, 5])
print(s2) #{1, 2, 3, 4, 5}

# For empty set
s = {}
print(s) #{}
print(type(s)) #<class 'dict'> - It will gives dict type

# So use set() func instead of {}
s = set()
print(s) #set()
print(type(s)) #<class 'set'>


# Do not allowed Duplicate value
s3 = {1,2,3,3,4,3,4,4,5,6,7}
print(s3) # {1, 2, 3, 4, 5, 6, 7}
# print(s3[0]) #Error - we can't access index (Set is unordered)


# Convert list into set & set don't allowed duplicate values
li = [1,2,3,4,5,6,7,1,2,3,4,5,6,1,4,7,5,9,6,3,5]
s2 = set(li)
print(s2) #{1, 2, 3, 4, 5, 6, 7, 9}
print(li) #[1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 1, 4, 7, 5, 9, 6, 3, 5]




# Different Methods - add, remove or discard, pop, clear

fruit = {"Apple", "Banana", "Lichi", "Orange", "Pear"}
print(fruit) #{'Lichi', 'Banana', 'Pear', 'Orange', 'Apple'} - unordered

# 1. add
fruit.add("Kiwi")
print(fruit) #{'Lichi', 'Banana', 'Pear', 'Kiwi', 'Orange', 'Apple'}

# 2. remove & discard
fruit.remove("Banana")
print(fruit) #{'Orange', 'Pear', 'Kiwi', 'Lichi', 'Apple'}
# fruit.remove("Grapes") #ERROR -> Grapes is not found

fruit.discard("Lichi")
print(fruit) #{'Apple', 'Pear', 'Orange', 'Kiwi'}
fruit.discard("Grapes")
print(fruit) #Grapes not founded still don't return ERROR

# 3. pop
fruit.pop() #Dlt random element
print(fruit)

# 4. clear
# fruit.clear()
# print(fruit) #set()


# sum(), min(), max() function
s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

print(sum(s)) #55
print(min(s)) #1
print(max(s)) #10





