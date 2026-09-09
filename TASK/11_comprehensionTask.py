# 1. Create a dictionary from 1 to 10, but include only even numbers as keys and their cubes as values. -> YES

dict = {x: x**3  for x in range (1,11) if x%2==0}
print(dict) 



# 2. Given a list of words, create a dictionary where key = word and value = length. -> YES

li = ["Amit", "Sumit", "Raj", "Jay", "Maya"]

dict = {x: len(x) for x in li}
print(dict)


# 3. Create a dictionary from 1 to 10:
# Even → "Even"
# Odd → "Odd" --> YES

evenOdd = {x: ("EVEN" if x % 2 == 0 else "ODD") for x in range(1, 11)}
print(evenOdd)



# 4. Swap keys and values of a dictionary.

dict = {"name":"Jugal", "age":21, "city": "G'ngr"}

dict2 = {v : k for k,v in dict.items()}
print(dict2)



# 5. Create a dictionary using two lists.

keys = ["name", "age", "city"]
values = ["Ram", 11, "Surat"]

dict={keys[i]: values[i] for i in range(len(keys))}
print(dict)



# 6. Count frequency of each character in a string.

str = "Mississippi"

dict = {ch : str.count(ch) for ch in str}
print(dict)



# 7. Count frequency of each word in a sentence.

sent = "Hello Wolrd Namaste Duniya Hello Duniya Namaste Python"
li = sent.split(" ")
print(li)

dict = {w : li.count(w) for w in li}
print(dict)



# 8. positive -> num, negative -> zero

li = [-3, 5, -1, 7]
op = []

output = [0 if i<0 else i for i in li]
print(output)



# 9. Greater than 10 -> "Big", else "small"

li = [1, 56, 3, 7, 15]

output = ["Big" if i<10 else "small" for i in li]
print(output)



# 10. Square if Even, cube if Odd

output = [i*i if i%2==0 else i**3 for i in range(1,11)]
print(output)
