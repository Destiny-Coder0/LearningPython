import statistics

students = [
    ["Mark", 20, 85],
    ["Thomas", 21, 90],
    ["Alice", 20, 40],
    ["Bob", 22, 78],
    ["Charlie", 19, 65],
    ["James", 22, 70],
    ["Adele", 23, 40],
    ["Mary", 21, 50],
    ["Johnny", 20, 30],
    ["Wendy", 19, 60]
]

scores=[]

for student in students:
    scores.append(student[2])

#Mean: Obtained by dividing the sum of all values ​​by the number of elements.
#Median: The middle value in the sorted data.
#Mode: The most repeated value.

mean_score=statistics.mean(scores)
median_score=statistics.median(scores)
mode_score=statistics.mode(scores)

above_avg = [student for student in students if student[2] > mean_score]
below_avg = [student for student in students if student[2] < mean_score]

top_student=max(students, key=lambda x: x[2])
low_student=min(students, key=lambda x: x[2])

closest_student = min(students, key=lambda x: abs(x[2] - mean_score))

print(f"Class mean is {mean_score}")
print(f"Class median is {median_score}")
print(f"Class mode is {mode_score}")

print("\n===== Students Above Average =====")
for student in above_avg:
    print(f"Name: {student[0]:<10} | Age: {student[1]:<3} | Score: {student[2]}")

print("\n===== Students Below Average =====")
for student in below_avg:
    print(f"Name: {student[0]:<10} | Age: {student[1]:<3} | Score: {student[2]}")

print(f"Student closest to average is {closest_student[0]} with a score of {closest_student[2]}")

print(f"Total number of students is {len(students)}")

print(f"Top student is {top_student[0]} with a score of {top_student[2]}")

print(f"Lowest student is {low_student[0]} with a score of {low_student[2]}")
