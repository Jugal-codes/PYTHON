# SNAKE, WATER, GUN GAME


import random as r

option = ['snake' , 'gun' , 'water']

computer = r.choice(option)
# print(computer)

user = input("Enter your choice:")

if user in option:
    # print(user)
    if computer == user:
        print("Draw")

    if computer =='snake' and user == 'water':
        print("Computer wins!")

    elif computer =='water' and user == 'snake':
       print("User wins!") 

    elif computer =='water' and user == 'gun':
        print("Computer wins!")

    elif computer =='gun' and user == 'water':
        print("User wins!") 

    elif computer =='snake' and user == 'gun':
        print("User wins!")

    elif computer =='gun' and user == 'snake':
        print("Computer wins!") 

else: 
    print("user choose wrong option!")


print(f"Computer chose {computer} & User chose {user}.")