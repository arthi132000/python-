contacts = {}

while True:
    print("\n1. Add  2. Display  3. Count  4. Exit")
    ch = input("Enter choice: ")

    if ch == '1':
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone
        print("Added")

    elif ch == '2':
        if len(contacts) > 0:
            for name, phone in contacts.items():
                print("Name:", name, "Phone:", phone)
        else:
            print("No contacts")

    elif ch == '3':
        print("Total Contacts:", len(contacts))

    elif ch == '4':
        print("Thank you!")
        break

    else:
        print("Invalid choice")
