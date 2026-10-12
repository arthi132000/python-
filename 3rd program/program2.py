correct_password = "Python123"
attempts = 3

while attempts > 0:
    password = input("Enter your password: ")

    if password == correct_password:
        print("Password Valid")

        encrypted = password[::-1]
        print("Encrypted Password:", encrypted)
        print("Login Successful")
        break

    else:
        attempts -= 1
        print("Invalid Password")
        print("Attempts left:", attempts)

if attempts == 0:
    print("Account Locked")
