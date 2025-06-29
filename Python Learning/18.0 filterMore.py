students = [
    ["Mark", 20, 85],
    ["Thomas", 21, 90],
    ["Alice", 20, 40],
    ["Bob", 22, 78],
    ["Charlie", 19, 65],
    ["James", 22, 70],
    ["Adele", 23, 45],
    ["Mary", 21, 50],
    ["Johnny", 20, 30],
    ["Wendy", 19, 60]
]

print("Welcome to the advanced sorting.")

students_sorted = sorted(students, key=lambda x: (x[1], x[2]))

print("\n===== Students Sorted by Age and Score =====")
for student in students_sorted:
    print(f"Name: {student[0]:<10} Age: {student[1]:<3} Score: {student[2]}")
