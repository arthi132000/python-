n = int(input("Enter number of students: "))

highest = 0

for i in range(1, n + 1):
    mark = float(input(f"Enter mark of student {i}: "))

    if mark > highest:
        highest = mark

print("\n--- Result ---")
print("Highest Mark =", highest)
