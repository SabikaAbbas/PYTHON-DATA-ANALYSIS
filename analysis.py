# Python Data Analysis Project

import pandas as pd

# Student data
data = {
    "Name": ["Ali", "Sara", "John", "Ayesha", "David"],
    "Math": [85, 92, 78, 88, 95],
    "Science": [80, 89, 75, 90, 91],
    "English": [82, 94, 80, 87, 93]
}

# Create a DataFrame
df = pd.DataFrame(data)

print("Student Data:")
print(df)

print("\nAverage Scores:")
print(df[["Math", "Science", "English"]].mean())

print("\nHighest Math Score:")
print(df["Math"].max())

print("\nHighest Science Score:")
print(df["Science"].max())

print("\nHighest English Score:")
print(df["English"].max())
