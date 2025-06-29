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

def filter(students, min_score, max_score):
    filtered = [student for student in students if min_score <= student[2] <= max_score]
    return filtered
    

print("Welcome to the score filter.")
min_score=int(input("Enter the minimum score: "))
max_score=int(input("Enter the maximum score: "))

filtered_students = filter(students, min_score, max_score)
filtered_students.sort(key=lambda student: student[2])

print("\n===== Students in Score Range =====")
for student in filtered_students:
    print(f"Name: {student[0]}, Age: {student[1]}, Score: {student[2]}")

if not filtered_students:
    print("No students found in the given range.")

    
