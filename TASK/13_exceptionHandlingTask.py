# TASK 1 - List Index :
# Create a list of 5 numbers.
# Ask the user to enter an index.

# Handle:
# IndexError
# ValueError

list = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter an index:"))
    try:
        print(list[index])
    except Exception as e:
        print("ERROR:", e)
except Exception as error:
    print("ERROR:", error)


# TASK 2 - Login System :
# Username : admin
# Password : 1234
# Raise an exception if the password is incorrect.

username = input("Enter user name:")
passw = int(input("Enter ur password:"))

print("User -> ",username)
try:
    if passw != 1234:
        raise ValueError("Password is incorrect.")
    print("Password -> ",passw)

except Exception as e:
    print("ERROR:" , e)


# TASK 3 - ATM System :
# Menu
# 1. Withdraw
# 2. Deposit
# 3. Balance

# Handle:
# Invalid input
# Insufficient balance
# Negative amount

class NegativeInputError(Exception):
    pass

balance = 5000

print("Select Correct Option:")
print("1. Withdraw\t 2. Deposite\t 3. Balance")

op = int(input("Enter correct option:"))

match op:
    case 1:
        print("You select withdraw..")
        try:
            w_amount = int(input("Enter withdraw amount:"))

            try:
                if w_amount < 0:
                    raise NegativeInputError("Amount cannot be negative")


                try:
                    if w_amount > balance:
                        raise Exception("Insufficient Balance")

                    balance -= w_amount
                    print("Amount withdrew..")
                    print("Current balance: ", balance)

                except Exception as err:
                    print("ERROR: ", err) 

            except NegativeInputError as er:
                print("ERROR: ", er)

        except Exception as e:
            print("ERROR", e)

    case 2:
        print("You select deposite..")

        try:
            d_amount = int(input("Enter deposite amount:"))
            try:
                if d_amount < 0:
                    raise NegativeInputError("Amount cannot be negative")
                
                balance += d_amount
                print("Current balance: ", balance)

            except NegativeInputError as err:
                print("ERROR: ", err)

        except Exception as e:
            print("ERROR", e)
    
    case 3:
        print("You select balance..")
        print(balance)
    case _:
        print("Invalid Choice!")