import math

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def multi(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return "Error: A number divided by 0 is undefined."
    return x / y

def exp(x, y):
    return x ** y

def mode(x, y):
    return x % y

def sqrrt(x):
    if x < 0:
        return "Error: The square root of a negative number cannot be taken."
    return math.sqrt(x)

print("=== CALCULATOR ===\n")

while True:
    print("\n1 - Addition (+)\n"
          "2 - Subtraction (-)\n"
          "3 - Multiplication (*)\n"
          "4 - Division (/)\n"
          "5 - Exponentiation (**)\n"
          "6 - Modulus (%)\n"
          "7 - Square Root (√¯)\n"
          "8 - Exit")

    try:
        choice = int(input("Which operation do you want to make (1-8)? "))

        if choice == 8:
            print("Calculator shutting down...")
            break

        if choice in range(1, 8):
            if choice == 7:
                x = float(input("Enter the number: "))
                print("Result:", sqrrt(x))
            else:
                x = float(input("Enter the first value: "))
                y = float(input("Enter the second value: "))

                if choice == 1:
                    print("Result:", add(x, y))
                elif choice == 2:
                    print("Result:", sub(x, y))
                elif choice == 3:
                    print("Result:", multi(x, y))
                elif choice == 4:
                    print("Result:", div(x, y))
                elif choice == 5:
                    print("Result:", exp(x, y))
                elif choice == 6:
                    print("Result:", mode(x, y))

        else:
            print("Invalid entry. Please enter a number between 1 and 8.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")
