password = input("Enter your password: ")

if len(password) >= 8:
    print("Strong Password")

    encrypted = password[::-1]

    print("Encrypted Password:", encrypted)
else:
    print("Weak Password")
