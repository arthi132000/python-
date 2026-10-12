n = int(input("Enter number of students: "))

lowest = float('inf')

for i in range(1, n + 1):
    mark = float(input(f"Enter mark of student {i}: "))

    if mark < lowest:
        lowest = mark

print("\n--- Result ---")
print("Lowest Mark =", lowest)
