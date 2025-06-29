numbers=[]

n=int(input("How many numbers do you want to enter? "))

for i in range(n):
    num=int(input(f"Enter the {i+1} number: "))
    numbers.append(num)

min_num=numbers[0]
max_num=numbers[0]

for num in numbers:
    if num<min_num:
        min_num=num
    elif num>max_num:
        max_num=num

print(f"The smallest number is {min_num}")
print(f"The biggest number is {max_num}")