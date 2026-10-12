import matplotlib.pyplot as plt

expenses = [40, 25, 20, 15]
categories = ['Food', 'Rent', 'Travel', 'Others']

plt.pie(expenses, labels=categories,
        autopct='%1.1f%%', startangle=90)
plt.title('Monthly Expense Distribution')
plt.show()