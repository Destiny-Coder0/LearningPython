students = [
    ["Mark", 20, 85],
    ["Thomas", 21, 90],
    ["Alice", 20, 40],
    ["Bob", 22, 78],
    ["Charlie", 19, 65]
]

top_student=students[0]

for student in students:
    if student[2]> top_student[2]:
        top_student=student

print("Student List: ")

for student in students:
    print(f"Name: {student[0]}, Age: {student[1]}, Score: {student[2]}")

print(f"Top student is: {top_student[0]} with score {top_student[2]}")