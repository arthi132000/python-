password = input("Enter your password: ")

if len(password) >= 8:
    print("Strong Password")

    encrypted = password[::-1]

    file = open("password.txt", "a")
    file.write(encrypted + "\n")
    file.close()

    print("Encrypted Password:", encrypted)
    print("Saved in file")

else:
    print("Weak Password (minimum 8 characters)")
