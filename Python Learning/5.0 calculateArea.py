def calculate_area(width, height):
    area= width * height
    return area

width = float(input("Enter the width: "))
height= float(input("Enter the height: "))

area=calculate_area(width, height)
print(f"The area of the rectangle is: {area}")