import pandas as pd
import numpy as np

# Create attendance data
data = {
    "Student": ["Arun", "Bala", "Kavi", "Divya", "Ravi"],
    "Present Days": [22, 20, 25, 23, 18],
    "Total Days": [25, 25, 25, 25, 25]
}

df = pd.DataFrame(data)

# Calculate attendance percentage
df["Attendance %"] = (
    np.array(df["Present Days"]) / np.array(df["Total Days"])
) * 100

print("STUDENT ATTENDANCE")
print(df)

print("\nAverage Attendance:", df["Attendance %"].mean())
