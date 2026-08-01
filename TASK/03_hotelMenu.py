# Using match, We create Hotel Menu

print("1 - Gujarati\n2 - Punjabi\n3 - Chinese\n4 - Italian\n5 - South_Indian")
dish = int(input("Choose your fav dish: "))
totalBill = 0

match dish:
    case 1:
        print("You Choose Gujarati!")

        print("1 - Undhiyu\n2 - Dhokla\n3 - Dal-Dhokli")
        choice = int(input("Enter ur choice for Gujarati dish:"))

        match choice:
            case 1:
                print("You choose Undhiyu__100Rs.")
            case 2:
                print("You choose Dhokla__120Rs.")
            case 3:
                print("You choose Dal-Dhokali__150Rs.")
            case _:
                print("Choose from available options...Please!!")
        
        order = int(input("How much plate u want to order??"))
        if choice == 1:
            totalBill = order * 100
        elif choice == 2:
            totalBill = order * 120
        elif choice == 3:
            totalBill = order * 150

                
    case 2:
        print("You Choose Punjabi!")

        print("1 - Chole Bhature\n2 - Paneer\n3 - Lassi")
        choice = int(input("Enter ur choice for Punjabi dish:"))

        match choice:
            case 1:
                print("You choose Chole Bhature__120Rs.")
            case 2:
                print("You choose Paneer__100Rs.")
            case 3:
                print("You choose Lassi__50Rs.")
            case _:
                print("Choose from available options...Please!!")
        
        order = int(input("How much plate u want to order??"))
        if choice == 1:
            totalBill = order * 120
        elif choice == 2:
            totalBill = order * 100
        elif choice == 3:
            totalBill = order * 50


    case 3:
        print("You Choose Chinese!")

        print("1 - Noodles\n2 - Manchurian\n3 - Spring Roll")
        choice = int(input("Enter ur choice for Chinese dish:"))

        match choice:
            case 1:
                print("You choose Noodles__150Rs.")
            case 2:
                print("You choose Manchurian__100Rs.")
            case 3:
                print("You choose Spring Roll__80Rs.")
            case _:
                print("Choose from available options...Please!!")
        
        order = int(input("How much plate u want to order??"))
        if choice == 1:
            totalBill = order * 150
        elif choice == 2:
            totalBill = order * 100
        elif choice == 3:
            totalBill = order * 80

    case 4:
        print("You Choose Italian!")

        print("1 - Pizza\n2 - Pasta\n3 - Tiramisu")
        choice = int(input("Enter ur choice for Italian dish:"))

        match choice:
            case 1:
                print("You choose Pizza__250Rs.")
            case 2:
                print("You choose Pasta__200Rs.")
            case 3:
                print("You choose Tiramisu__300Rs.")
            case _:
                print("Choose from available options...Please!!")
        
        order = int(input("How much plate u want to order??"))
        if choice == 1:
            totalBill = order * 250
        elif choice == 2:
            totalBill = order * 200
        elif choice == 3:
            totalBill = order * 300


    case 5:
        print("You Choose South_Indian!")

        print("1 - Idali\n2 - Dosa\n3 - Medu vada")
        choice = int(input("Enter ur choice for South_Indian dish:"))

        match choice:
            case 1:
                print("You choose Idali__100Rs.")
            case 2:
                print("You choose Dosa__150Rs.")
            case 3:
                print("You choose Medu vada__100Rs.")
            case _:
                print("Choose from available options...Please!!")
        
        order = int(input("How much plate u want to order??"))
        if choice == 1:
            totalBill = order * 100
        elif choice == 2:
            totalBill = order * 150
        elif choice == 3:
            totalBill = order * 100

    case _:
        print("Please choose correct option...")



print(f"Your total bill is {totalBill}.")