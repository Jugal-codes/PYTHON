# Raise exception

# Example - 1
age = 5
# age = -5    # gives ERROR & stop the code bc absence of try except
if age < 0:
    raise ValueError("Age can not be negative")

print("Valid Age")


# Example - 2
balance = 500
withdraw = 1000

try:
    if withdraw > balance:
        raise Exception("Insufficient Balance")
except Exception as e:
    print("Error :", e)


# Example - 3
try:
    age = int(input("Enter Age: "))

    if age < 18:
        raise ValueError("You are not eligible")
    print("Eligible")

except ValueError as e:
    print("Error:", e)




# User-defined exception
class InvalidMarksError(Exception):
    pass

marks = -10
try:
    if marks < 0:
        raise InvalidMarksError("Marks cannot be negative")
except InvalidMarksError as e:
    print("Error :", e)


# Exmaple - 2
balance = 5000

try:
    amount = int(input("Enter withdrawal amount: "))

    if amount > balance:
        raise Exception("Insufficient Balance")
    
    balance -= amount
    print("Remaining Balance:", balance)

except Exception as e:
    print(e)




#  Nested try except
# Example - 1
try:
    print("Outer Try")

    try:
        print(10 / 0)
    except ZeroDivisionError:
        print("Inner Except: Cannot divide by zero")

except:
    print("Outer Except")



# Example - 2 
try:
    print("Outer Try")

    try:
        num = int("abc")
    except ZeroDivisionError:
        print("Inner Except")

except ValueError:
    print("Outer Except: Invalid Number")


# Example - 3
try:
    file = open("data.txt")

    try:
        data = int(file.read())
        print(data)
    except ValueError:
        print("File contains invalid data")
    finally:
        file.close()
        print("File Closed")

except FileNotFoundError:
    print("File Not Found")
