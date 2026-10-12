import matplotlib.pyplot as plt

students = ['Arun', 'Bala', 'Cathy', 'David']
marks = [85, 70, 90, 75]

plt.bar(students, marks, color='green')
plt.title('Student Marks Comparison')
plt.xlabel('Students')
plt.ylabel('Marks')
plt.show()