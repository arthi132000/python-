contacts = {}

while True:
    print("\n1. Add  2. Search  3. Display  4. Exit")
    ch = input("Enter choice: ")

    if ch == '1':
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")

        contacts[name] = [phone, email]
        print("Added")

    elif ch == '2':
        name = input("Name to search: ")

        if name in contacts:
            print("Phone:", contacts[name][0])
            print("Email:", contacts[name][1])
        else:
            print("Not found")

    elif ch == '3':
        for name, details in contacts.items():
            print("Name:", name)
            print("Phone:", details[0])
            print("Email:", details[1])

    elif ch == '4':
        print("Thank you!")
        break

    else:
        print("Invalid choice")