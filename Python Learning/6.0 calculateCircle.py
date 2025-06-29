#Calculating the area and circumference of a circle
#Area=pi*r^2 , circumference=2pi*r, pi=3.14

def calculate_area(r, pi):
    areaC = pi*(r**2)
    return areaC

def calculate_circum(r, pi):
    circumC = 2*pi*r
    return circumC

r = int(input("What's the radius of the circle? "))
pi = 3.14

print(f"Area of the circle is {calculate_area()}")
print(f"Circumference of the circle is {calculate_circum()}")

