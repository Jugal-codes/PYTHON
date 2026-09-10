"""
5. Write a program to make Rock Paper Scissors game

com = rock
user = paper

if com == user:
    draw

if (user == "R" and com == "S") or (user == "P" and com == "R") or (user == "S" and com == "p"):
    user win
else
    com win
"""

# 1. Write a program to generate a 4-digit OTP.
import random as r
print("Your OTP for verfication is : ", r.randint(1000,9999))



# 2. Write a program to make Lottery Game :
'''
Generate 5 random numbers (1 - 50).
li = [34,23,45,12,37]

Ask user to guess numbers.
for i in range(1,6):

Check how many matches.
'''
import random as r

li = []
for i in range(1,6):
    li.append(r.randint(1,50))
print(li)

li2 = []
match = 0
for i in range(1,6):
    gNum = int(input("Guess the number btw 1 to 50:"))
    # li2.append(gNum)
    for i in li:
        if i==gNum:
            match += 1
            li2.append(gNum)
print(f"Match num:{match} => {li2}")     



# 3. Write a program to generate a random HEX color code like #A3F4C1.
import random as r

hexCode = "0123456789ABCDEF"

str = r.choices(hexCode, k=6)
result = "".join(str)

print("Hex code is: #",result)



# 4. Write a program to guess the Number Game
'''
randomNo = 1 to 25 (18)
while True:
    no = 16 -> Too Low
    no -> 20 -> To High
    no = 18 -> Break
'''
import random as r

rNum = r.randint(1,25)

while True:
    Number = int(input("Guess the number btw 1 to 25:"))
    print(Number)

    if Number > rNum:
        print("Too High")
    elif Number < rNum:
        print("Too Low")
    else:
        print("Correct Guess!!")
        break



# 5. Write a program to make Rock Paper Scissors game
'''
com = rock , user = paper
if com == user:
    draw
if (user == "R" and com == "S") or (user == "P" and com == "R") or (user == "S" and com == "p"):
    user win
else
    com win
'''
import random as r

list = ["Rock", "Paper", "Scissors"]
com = r.choice(list)

user = input("Choose any one from 'Rock, Paper, Scissors' -> ")
print("User choice:", user)

if com == user:
    print("Draw")
elif (user == "Rock" and com == "Scissor") or (user == "Paper" and com == "Rock") or (user == "Scissor" and com == "Paper"):
    print("User win!")
else:
    print("Computer win!")



