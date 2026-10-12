import pandas as pd
import numpy as np

# Create student data
data = {
    "Name": ["Arun", "Bala", "Kavi", "Divya", "Ravi"],
    "Maths": [85, 75, 90, 80, 70],
    "Science": [80, 70, 95, 85, 75]
}

df = pd.DataFrame(data)

# Calculate total and average
df["Total"] = np.array(df["Maths"]) + np.array(df["Science"])
df["Average"] = np.array(df["Total"]) / 2

print("STUDENT MARKS")
print(df)

print("\nClass Total:", df["Total"].sum())
print("Class Average:", df["Average"].mean())
