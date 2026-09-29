# In no1/no2 condition, if we gives no1 = 10 & no2 = 0 then it will gives Error..
# To handle this type of ERROR, we use exception --> try: except: 

# Without using Exception
'''
no1 = int(input("Enter a number 1 : "))     # 10
no2 = int(input("Enter a number 2 : "))     # 0

print("Start")
# print(no1 / no2)    # Gives Error
print("End")
'''


# Using Exception

# First approach:
no1 = int(input("Enter a number 1 : "))
no2 = int(input("Enter a number 2 : "))

print("Start")
try:
    print(no1 / no2)
except:
    print("ERROR")

print("End")


# Second approach:
try:
    no1 = int(input("Enter a number 1 : "))
    no2 = int(input("Enter a number 2 : "))
    print("Start")
    print(no1 / no2)
except ZeroDivisionError:
    print("division by zero")
except ValueError:
    print("invalid number")
print("End")


# Third approach:
try:
    num = int(input("Enter Number: "))
    print(10 / num)

except (ValueError, ZeroDivisionError):
    print("Invalid Input")


# We can print actual ERROR also:
try:
    x = 10 / 0      # Error: division by zero
    x = 10 / 10     # 1.0
    print(x)

except Exception as e:
    print("Error:", e)





# We can filter Error like:
#   If this type of error occur then gives ERROR 
#   Otherwise gives RESULT
# For this we use,  try  ->  except ERROR_NAME  ->  else 

try:
    num = int(input("Enter Number: "))
    result = 10 / num

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Result =", result)



# To execute whole code if there is error or not
# Then use,     try  ->  except  ->  finally

try:
    print(10 / 0)

except:
    print("Error")

finally:
    print("Always Executes")
