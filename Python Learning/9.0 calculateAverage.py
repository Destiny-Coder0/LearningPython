def calculate_average(numbers):
    total=0
    for i in numbers:
        total = total+i
    average=total/len(numbers)
    return average

n = int(input("How many numbers do you want to enter? "))
numbers=[]

for i in range(n):
    num=int(input(f"Enter number {i+1}: "))
    numbers.append(num)

average = calculate_average(numbers)
print(f"The average of the numbers is: {average}")