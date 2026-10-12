correct_pin = 1234
balance = 5000

pin = int(input("Enter your PIN: "))

if pin == correct_pin:

    while True:
        print("\n===== ATM MENU =====")
        print("1. Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Balance =", balance)

        elif choice == 2:
            amount = float(input("Enter amount: "))

            if amount <= balance and amount > 0:
                balance -= amount
                print("Withdrawal Successful")
            else:
                print("Insufficient Balance")

        elif choice == 3:
            amount = float(input("Enter amount: "))

            if amount > 0:
                balance += amount
                print("Deposit Successful")
            else:
                print("Invalid Amount")

        elif choice == 4:
            print("Thank you!")
            break

        else:
            print("Invalid Choice")

else:
    print("Incorrect PIN")
