1. Line Chart – Sales Trend
python
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [100, 150, 120, 180, 220]

plt.plot(months, sales, marker='o', color='blue')
plt.title('Monthly Sales Trend')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.grid(True)
plt.show()