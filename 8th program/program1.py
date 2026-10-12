import matplotlib.pyplot as plt

# Student data
students = ["Arun", "Bala", "Kavi", "Divya", "Ravi"]
marks = [85, 75, 90, 80, 70]

# Create dashboard
plt.figure(figsize=(12, 8))

# Line Chart
plt.subplot(2, 2, 1)
plt.plot(students, marks, marker="o", color="blue")
plt.title("Student Marks - Line Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.grid()

# Bar Chart
plt.subplot(2, 2, 2)
plt.bar(students, marks, color="green")
plt.title("Student Marks - Bar Chart")
plt.xlabel("Students")
plt.ylabel("Marks")

# Pie Chart
plt.subplot(2, 2, 3)
plt.pie(marks, labels=students, autopct="%1.1f%%")
plt.title("Student Marks - Pie Chart")

plt.suptitle("STUDENT PERFORMANCE DASHBOARD")
plt.tight_layout()
plt.savefig("program1.png")
plt.show()


