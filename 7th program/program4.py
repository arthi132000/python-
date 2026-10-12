import pandas as pd
import numpy as np

# Create electricity usage data
data = {
    "House": ["House 1", "House 2", "House 3", "House 4", "House 5"],
    "Units": [100, 150, 200, 120, 180],
    "Rate": [6, 6, 6, 6, 6]
}

df = pd.DataFrame(data)

# Calculate electricity bill
df["Bill"] = np.array(df["Units"]) * np.array(df["Rate"])

print("ELECTRICITY BILL DATA")
print(df)

print("\nTotal Electricity Bill:", df["Bill"].sum())
