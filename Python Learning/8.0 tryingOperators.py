#What is the difference between the multiplication of the two numbers you received from the user and the sum of x,y,z?
#Calculate the division of y by x without a remainder
#What is the sum of x, y, z mod 3?
#Calculate y to the xth power.

def division(y,x):
    return y//x

def mod(sum):
    return sum%3

def y_to_xth(x,y):
    return y**x

x,y,z=3,4,5

sum= x+y+z

num1 = int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))

multi=num1*num2

result=multi-sum

print(f"The difference between them is {result} ")

print(f"y/x without remainder is {division(y,x)}")

print(f"x+y+z%3 is {mod(sum)}")

print(f"y^x is {y_to_xth(x,y)}")


