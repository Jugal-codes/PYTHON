# How to create a dictionary
# Approach 1:
user = {"Name": "Ram", "Age": 21, "City": "Ahm"}
print(user) #{'Name': 'Ram', 'Age': 21, 'City': 'Ahm'}
print(type(user)) #<class 'dict'>

# Approach 2:
person = dict(name="Shyam", age="22")
print(person) #{'name': 'Shyam', 'age': '22'}


# print empty dict
d = {}
print(d) #{}
print(type(d)) #<class 'dict'>




# Access each key nd value from the dict
# 1st way 
print (user["Name"]) #Ram
print (person["age"]) #22
# print(person["State"]) #Error

# 2nd way
print(person.get("name")) #Shyam
print(person.get("State")) #None - if given key isn't exist in get() then gives default value -> None
#  We can change default value
print(user.get("address", "Not Found")) #Not Found
 



user = {
    "name" : "Jug",
    "age" : 21,
    "city" : "G'nagr",
    "State" : "Gujarat",
    "Country" : "India",
}
print(user) #{'name': 'Jug', 'age': 21, 'city': "G'nagr", 'State': 'Gujarat', 'Country': 'India'}

# change value of key
user["city"] = "Pln"
print("updated user => ",user) #updated user =>  {'name': 'Jug', 'age': 21, 'city': 'Pln', 'State': 'Gujarat', 'Country': 'India'}

# change value of keys nd if not exist then it will add
user.update({"age":22, "State":"RJ", "Gender": "Female"})
print(user) #{'name': 'Jug', 'age': 22, 'city': 'Pln', 'State': 'RJ', 'Gender': 'Female'}


# Deleting items
# 1. del 
del user["Country"] 
# print(user["Country"]) #Error
print(user) #{'name': 'Jug', 'age': 22, 'city': 'Pln', 'State': 'RJ', 'Gender': 'Female'}

# 2. Pop -> delete choosen key only
pop_value = user.pop("city")
print(pop_value) #Pln
print(user) #{'name': 'Jug', 'age': 22, 'State': 'RJ', 'Gender': 'Female'}

# 3. Popitem -> delete last value
pop_item = user.popitem()
print(pop_item) #('Gender', 'Female')
print(user) #{'name': 'Jug', 'age': 22, 'State': 'RJ'}

# clear -> delete all key-value pairs
# user.clear()
# print(user)




# Looping Through a Dictionary 
user = {
    "name" : "Jug",
    "age" : 21,
    "city" : "G'nagr",
    "State" : "Gujarat",
    "Country" : "India",
}

# Loop over keys --> gives only keys
for i in user:
    print(i, end = " ") #name age city State Country
print()

# another for keys
for i in user.keys():
    print(i, end = " ") #name age city State Country
print()

# Loop over values --> gives only values
for i in user.values():
    print(i, end = " ") #Jug 21 G'nagr Gujarat India
print()

# Loop over key-value pairs --> gives each pair
for i in user.items():
    print(i, end = " ") #('name', 'Jug') ('age', 21) ('city', "G'nagr") ('State', 'Gujarat') ('Country', 'India') 
print()





# if keys list nd value list are given then how to convert it into dict
keys = ["Name", "City", "State"]
values = ["Jug", "G'nagr", "Gujarat"]

user_data = dict(zip(keys, values))
print(user_data) #{'Name': 'Jug', 'City': "G'nagr", 'State': 'Gujarat'}



# In dict, keys can be string, number and tuple 
# But keys can't be list, dictionary and set
dict = {
    "person": {"Name": "Shyam", "Age": 21},
    "Address": {"City": "Ahm", "State": "Guj"},
}

print(dict) #{'person': {'Name': 'Shyam', 'Age': 21}, 'Address': {'City': 'Ahm', 'State': 'Guj'}}
print(dict["person"]["Name"]) #Shyam
print(dict["person"].get("Name")) #shyam
print(dict["Address"]) #{'City': 'Ahm', 'State': 'Guj'}


