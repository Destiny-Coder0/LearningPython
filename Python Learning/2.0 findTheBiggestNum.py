nums = []

for i in range(5):
    num = int(input(f"Enter the {i} number: "))
    nums.append(num)

max = nums[0]

for num in nums:
    if num > max:
        max = num


print(f"Your numbers: {nums}")
print(f"Max number is {max}")