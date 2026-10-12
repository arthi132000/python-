while True:
    print("\n===== ELECTRICITY MENU =====")
    print("1. Calculate Bill")
    print("2. Check Rate")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        units = float(input("Enter units consumed: "))

        if units <= 100:
            bill = units * 2
        elif units <= 200:
            bill = units * 3
        else:
            bill = units * 5

        print("Electricity Bill =", bill)

    elif choice == 2:
        print("Rate: 100 units = Rs.2 per unit")
        print("Rate: 101-200 units = Rs.3 per unit")
        print("Above 200 units = Rs.5 per unit")

    elif choice == 3:
        print("Thank you!")
        break

    else:
        print("Invalid choice. Try again!")
