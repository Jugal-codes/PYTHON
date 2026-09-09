#  Comprehension - shorter way to write collection like dict, list and set (tuple aren't inclued)


# For List
# In normal way
li = []
for i in range(1, 11):
    li.append(i * i)
print(li) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# In Comprehension way
li2 = [i * i for i in range(1, 11)]
print((li2)) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# example - print even value only -> for only with if stt
even = []
for i in range(1,16):
    if i%2==0:
        even.append(i)
print(even) #[2, 4, 6, 8, 10, 12, 14]

# In Comprehension way
even2 = [i for i in range (1,16) if i%2==0]
print(even2) #[2, 4, 6, 8, 10, 12, 14]


# example - print even odd  -> for with if .. else stt
num = [12,45,78,97,54,1,44,89,98,79]
evenOdd = []
for i in num:
    if i%2==0:
        evenOdd.append("EVEN")
    else:
        evenOdd.append("ODD")
print(evenOdd) #['EVEN', 'ODD', 'EVEN', 'ODD', 'EVEN', 'ODD', 'EVEN', 'ODD', 'EVEN', 'ODD']

# In Comprehension way
evenOdd2 = ["EVEN" if i%2==0 else "ODD" for i in num]
print(evenOdd2) #['EVEN', 'ODD', 'EVEN', 'ODD', 'EVEN', 'ODD', 'EVEN', 'ODD', 'EVEN', 'ODD']


# example - print grade  -> for with if .. elif .. else stt
marks = [90, 56, 78, 66, 25, 95, 45, 67, 34, 79]
grade = []
for i in marks:
    if i >= 80:
        grade.append("Grade A")
    elif i >= 60:
        grade.append("Grade B")
    elif i >= 50:
        grade.append("Grade C")
    elif i >= 40:
        grade.append("Grade D")
    else:
        grade.append("Fail")
print(grade) #['Grade A', 'Grade C', 'Grade B', 'Grade B', 'Fail', 'Grade A', 'Grade D', 'Grade B', 'Fail', 'Grade B']

grade2 = ["Grade A" if i>=80 else "Grade B" if i>=60 else "Grade C" if i>=50 else "Grade D" if i>=40 else "Fail" for i in marks]
print(grade2) #['Grade A', 'Grade C', 'Grade B', 'Grade B', 'Fail', 'Grade A', 'Grade D', 'Grade B', 'Fail', 'Grade B']



# FOR SET - set is unordered
s = {i * i for i in range(1, 11)}
print(s) #{64, 1, 4, 36, 100, 9, 16, 49, 81, 25}


# FOR DICT
d = {x: x * x for x in range(1, 11)}
print(d) #{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

even = {x: x * x for x in range(1, 11) if x % 2 == 0}
print(even) #{2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

evenOdd = {x: (x * x if x % 2 == 0 else x**3) for x in range(1, 11)}
print(evenOdd) #{1: 1, 2: 4, 3: 27, 4: 16, 5: 125, 6: 36, 7: 343, 8: 64, 9: 729, 10: 100}


