# Learn Methods :
'''
1. dict.get()
2. dict.keys()
3. dict.values()
4. dict.items()
5. dict.update(other_dict)
6. dict.pop(key, default)
7. dict.popitem()
8. dict.clear()
9. dict.copy()
10. dict.fromkeys(keys, value)
11. dict.setdefault(key, default)
12. len(dict)
'''

user = {
    "name" : "Jugl",
    "age" : 21,
    "city" : "G'nagr",
    "State" : "Gujarat",
    "Country" : "India",
}
print(user) #{'name': 'Jugl', 'age': 21, 'city': "G'nagr", 'State': 'Gujarat', 'Country': 'India'}

# 1. dict.get(key, default) : default if key doesn't exist
print(user.get("name")) #Jugl
print(user.get("Marks","Not Found")) #Not Found

# 2. dict.keys() : return all keys
print(user.keys()) #dict_keys(['name', 'age', 'city', 'State', 'Country'])

# 3. dict.values() : return all values
print(user.values()) #dict_values(['Jugl', 21, "G'nagr", 'Gujarat', 'India'])

# 4. dict.items() : return key-value pairs as tuple
print(user.items()) #dict_items([('name', 'Jugl'), ('age', 21), ('city', "G'nagr"), ('State', 'Gujarat'), ('Country', 'India')])

# 5. dict.update(other_dict) : update existing keys otherwise add key-value pair
user.update({"city":"Ahmedabad", "Marks":8.9})
print(user) #{'name': 'Jugl', 'age': 21, 'city': 'Ahmedabad', 'State': 'Gujarat', 'Country': 'India', 'Marks': 8.9}

# 6. dict.pop(key, default) : if key not exist return default
print(user.pop("Marks")) #8.9
print(user.pop("fname","key not found")) #key no found

# 7.dict.popitem() : remove last inserted key-value pair
print(user.popitem()) #('Country', 'India')

# 8. dict.clear() : dlt all pairs nd gives empty dict
# user.clear()
# print(user) #{}

# 9. dict.copy()
user1 = user.copy()
user1["city"] = "Udaipur"
user1["State"] = "Rajasthan"
print(user) #{'name': 'Jugl', 'age': 21, 'city': 'Ahmedabad', 'State': 'Gujarat'}
print(user1) #{'name': 'Jugl', 'age': 21, 'city': 'Udaipur', 'State': 'Rajasthan'}

# 10. dict.fromkeys(keys,value) : create a new dict  
keys = {"Math", "Bio", "Phy", "Chem"}
total = dict.fromkeys(keys, 100)
print(total)

# 11. dict.setdefault(key, default) : return value of key, 
#                                     if key doesn't exit then return None (can set default value)
print(user.setdefault("name"))
# print(user.setdefault("fname")) #None
# print(user) #{'name': 'Jugl', 'age': 21, 'city': 'Ahmedabad', 'State': 'Gujarat', 'fname': None}
print(user.setdefault("fname", "Chaudhary")) #Chaudhary
print(user) #{'name': 'Jugl', 'age': 21, 'city': 'Ahmedabad', 'State': 'Gujarat', 'fname': 'Chaudhary'}

# 12. len(dict) : check lenght of dict
print(len(user)) 



print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
