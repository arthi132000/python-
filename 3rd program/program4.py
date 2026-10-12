password = input("Enter your password: ")

special = "!@#$%^&*"

if len(password) >= 8:
    if any(ch.isupper() for ch in password):
        if any(ch.islower() for ch in password):
            if any(ch.isdigit() for ch in password):
                if any(ch in special for ch in password):
                    print("Very Strong Password")

                    encrypted = password[::-1]
                    print("Encrypted Password:", encrypted)
                else:
                    print("Add a special character")
            else:
                print("Add a number")
        else:
            print("Add a lowercase letter")
    else:
        print("Add an uppercase letter")
else:
    print("Minimum 8 characters required")
