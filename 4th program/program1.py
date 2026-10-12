contacts = {}

while True:
    print("\n1. Add  2. Search  3. Delete  4. Exit")

    ch = input("Enter choice: ")

    if ch == '1':
        name = input("Name: ")
        phone = input("Phone: ")

        contacts[name] = phone
        print("Added")

    elif ch == '2':
        name = input("Name to search: ")

        if name in contacts:
            print("Phone:", contacts[name])
        else:
            print("Not found")

    elif ch == '3':
        name = input("Name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Deleted")
        else:
            print("Not found")

    elif ch == '4':
        print("Thank you!")
        break

    else:
        print("Invalid choice")
