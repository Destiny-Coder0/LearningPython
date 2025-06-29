numbers=[-10, 2, 5, -5, -9, 23, 12, -3, 18]

positive_num=[]

for num in numbers:
    if num>0:
        positive_num.append(num)

positive_num.sort()
print(f"Positive numbers are {positive_num}")