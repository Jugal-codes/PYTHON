# Using multiple if statement -> Count notes
'''
Example ==> Amout = 1360
n500 -> 2 -> 1360 - 1000 -> 260
n200 -> 1 -> 360 - 200 -> 160
n100 -> 2 -> 160 - 100 -> 60
n50 -> 1 -> 60 - 50 -> 10
n20 -> 0
n10 -> 1 -> 10 - 10 -> 0
n5 -> 0
n2 -> 0
n1 -> 0
'''


amt = int(input("Enter your amount:"))
n500 = n200 = n100 = n50 = n20 = n10 = n5 = n2 = n1 = 0

if amt >= 500:
    n500 = amt // 500   #n500 = 1365 // 500 -> = 2
    amt %= 500          # 1365 % 500 -> 365

if amt >= 200:
    n200 = amt // 200 
    amt %= 200

if amt >= 100:
    n100 = amt // 100 
    amt %= 100

if amt >= 50:
    n50 = amt // 50
    amt %= 50

if amt >= 20:
    n20 = amt // 20
    amt %= 20

if amt >= 10:
    n10 = amt // 10
    amt %= 10

if amt >= 5:
    n5 = amt // 5
    amt %= 5

if amt >= 2:
    n2 = amt // 2
    amt %= 2
    
if amt >= 1:
    n1 = amt // 1
    amt %= 1

print("Note of 500:",n500)
print("Note of 200:",n200)
print("Note of 100:",n100)
print("Note of 50:",n50)
print("Note of 20:",n20)
print("Note of 10:",n10)
print("Note of 5:",n5)
print("Note of 2:",n2)
print("Note of 1:",n1)


# amt = int(input("ENter amount:"))
# n500 = n200 = n100 = n50 = n20 = n10 = n5 = n2 = n1 = 0

# if amt >= 500:
#     n500 = amt - amt % 500 
#     c500 = n500 // 500
#     amt -= n500
#     print(n500)
#     print(amt)
# if amt >= 200:
#     pass

# # print(f"Note of 500: {c500}")
# # print(n200)




