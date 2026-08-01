# match work like switch statement. It’s called Structural Pattern Matching.
# SYNTAX :
'''
match variable:
    case pattern1:
        # code block
    case pattern2:
        # code block
    case _:
        # default block (like "else")
'''

# Example - 1 : Print weekday name

day = int(input("Enter a day number between 1 to 7 : "))
match day:
    case 1:
        print("MON")
    case 2:
        print("TUE")
    case 3:
        print("WED")
    case 4:
        print("THU")
    case 5:
        print("FRI")
    case 6:
        print("SAT")
    case 7:
        print("SUN")
    case _:
        print("Invalid Day Number")



# Example - 2 : Print odd/even for given number

num = int(input("Enter a number:"))
match num:
    case n if n % 2 == 0:
        print(f"{n} is Even")
    case n if n % 2 != 0:
        print(f"{n} is Odd")



