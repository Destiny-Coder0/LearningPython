numbers=[-10, 1, 20, 3, 6, -9, 5, 2, -3, 8, -4]

even_num=[]
odd_num=[]

for num in numbers:
    if num%2==0:
        even_num.append(num)
    else:
        odd_num.append(num)


even_num.sort()
odd_num.sort()

print(f"Even numbers are {even_num}")
print(f"Odd numbers are {odd_num}")
