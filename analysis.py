# Python Data Analysis Project

students = {
    "Name": ["Ali", "Sara", "John", "Ayesha", "David"],
    "Math": [85, 92, 78, 88, 95],
    "Science": [80, 89, 75, 90, 91],
    "English": [82, 94, 80, 87, 93]
}

print("Student Data:")
print(students)

print("\nMath Scores:")
print(students["Math"])

print("\nHighest Math Score:")
print(max(students["Math"]))

print("\nAverage Math Score:")
print(sum(students["Math"]) / len(students["Math"]))
