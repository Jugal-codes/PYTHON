# 1. Count Frequency of Characters
# word = "python"
# freq = {
#     "p":1
#     "y":1 .. so on
# }

word = "madam"
d = {}

for i in word:
    d[i] = d.get(i, 0) + 1
print(d)




# 2. Count Frequency of Words
# sentence = "python is easy python is powerful"

sentence = "python is easy python is powerful"
li = sentence.split()
d = {}

for i in li:
    d[i] = d.get(i, 0) + 1
print(d)




# 3. Create Dictionary of Number and Cube
# data = {}
# data = {
#     1:1,
#     2:8,
#     3:27
# }

data = {}
for i in range(1, 11):
    data[i] = i**3
print(data)




# 4. Swap Keys and Values
# data = {"a": 1,"b": 2, "c": 3}

data = {"a": 1, "b": 2, "c": 3}
d = {}

for k, v in data.items():
    d[v] = k
print(d)




# 5. Find Duplicate Values
# data = {
#     "a": 10,
#     "b": 20,
#     "c": 10,
#     "d": 30
# }

data = {"a": 10, "b": 20, "c": 10, "d": 20}
duplicate = []
values = list(data.values())

for i in values:
    if values.count(i) > 1 and i not in duplicate:
        duplicate.append(i)
print(duplicate)




# 6. Create Dictionary From String Length
# words = ["python", "java", "ai"]

# data = {
#     "Python":6
# }

words = ["python", "java", "ai"]
d = {}

for word in words:
    d[word] = len(word)
print(d)




# 7. Count Vowels in Sentence
# sentence = "python programming"

# !st Approach : 
sentence = "python programming"
li = sentence.split()
v = 0
print(li)

for i in li:
   for j in i:
       if j in 'AEIOUaeoiu':
           v += 1
           # print(j)
print("Vowels in sentance:",v)


# 2nd Approach :
sent = "python programming"
v = 0

for ch in sent:
    if ch in 'AEIOUaeiou':
        v += 1
print("Vowels in sentance:",v)




# 8. Create Dictionary of Factorials
# data = {
#     1:1,
#     2:2,
#     3:6,
#     4:24,
#     5:120
# }
# fact = 1*2*..*n

data = {}
fact = 1

for i in range(1, 11):
    fact = fact * i
    data[i] = fact
print(data)




# 9. Group Numbers by Positive and Negative
# numbers = [10, -5, 7, -2, 0]

# data = {
#     "positive": [],
#     "negative": [],
#     "zero": []
# }

numbers = [10, -5, 7, -2, 0]
print(numbers)

data = {
    "positive": [],
    "negative": [],
    "zero": []
}

for i in numbers:
    if i > 0:
        data["positive"].append(i)
    elif i < 0:
        data["negative"].append(i)
    else:
        data["zero"].append(i)
print(data)




# 10. Separate Even and Odd Numbers ---> YES
# numbers = [1, 2, 3, 4, 5, 6]

# data = {
#     "even": [],
#     "odd": []
# }

numbers = [1, 2, 3, 4, 5, 6]
print(numbers)

even = []
odd = []

for i in numbers:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)