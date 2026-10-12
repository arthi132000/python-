import pandas as pd
import numpy as np

# Create stock data
data = {
    "Product": ["Pen", "Book", "Bag", "Pencil", "Eraser"],
    "Quantity": [100, 50, 20, 80, 60],
    "Price": [10, 50, 500, 5, 3]
}

df = pd.DataFrame(data)

# Calculate stock value
df["Stock Value"] = np.array(df["Quantity"]) * np.array(df["Price"])

print("STOCK DATA")
print(df)

print("\nTotal Stock Value:", df["Stock Value"].sum())
