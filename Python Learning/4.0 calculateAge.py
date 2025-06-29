from datetime import datetime

def calculate_age(birthYear):
    currentYear = datetime.now().year
    age = currentYear - birthYear
    return age

birthYear = int(input("Enter your birth year: "))

age = calculate_age(birthYear)
print(f"You are {age} years old!")