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

total=0

for student in students:
    total += student[2]

average_score = total/len(students)

print(f"The class average is {average_score}")

print("Students with scores higher than the class average: ")
for student in students:
    if student[2] > average_score:
        print(f"Name: {student[0]}, with score {student[2]}")
