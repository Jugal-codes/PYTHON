# MAJOR TASK : 
dict = {
    "Virat": [98, 67, 56, 78, 77],
    "Dhoni": [45, 98, 88, 79, 67],
    "Rohit": [87, 66, 59, 45, 23],
}
print(dict)

# Qs 1 : Update the score of Dhoni 
dict["Dhoni"][2] = 77
print(dict)


# Qs 2 : Print sum of each player's score
for i in dict:
    sum = 0
    print(i, "->", dict[i])
    for j in dict[i]:
        sum += j
        # print(j)
    print(sum)


# Qs 3 : Print Total of all player's score
total_s = 0
for i in dict:
    sum = 0
    print(i, "->", dict[i])
    for j in dict[i]:
        sum += j
        # print(j)
    print(sum)
    total_s += sum
print(total_s)