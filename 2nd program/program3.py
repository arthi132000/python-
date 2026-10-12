total = 0

while True:
    print("\n===== SHOPPING MENU =====")
    print("1. Add Item")
    print("2. View Total")
    print("3. Checkout")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        price = float(input("Enter item price: "))

        if price > 0:
            total += price
            print("Item added successfully")
        else:
            print("Invalid price")

    elif choice == 2:
        print("Current Total =", total)

    elif choice == 3:
        if total >= 1000:
            discount = total * 0.10
            final_amount = total - discount
            print("10% Discount Applied")
        else:
            final_amount = total

        print("Final Amount =", final_amount)

    elif choice == 4:
        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice. Try again!")
