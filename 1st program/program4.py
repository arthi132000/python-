n = int(input("Enter number of subjects: "))
total = 0
pass_count = 0
fail_count = 0

for i in range(1, n + 1):
    mark = float(input(f"Enter marks for subject {i}: "))
    total += mark

    if mark >= 50:
        pass_count += 1
    else:
        fail_count += 1

average = total / n

if average >= 90:
    grade = "A+"
elif average >= 75:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "Fail"

print("\n--- Result ---")
print("Total Marks =", total)
print("Average =", average)
print("Grade =", grade)
print("Pass Subjects =", pass_count)
print("Fail Subjects =", fail_count)
