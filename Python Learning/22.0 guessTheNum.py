'''
Try to find a randomly generated number between 1-100 with more or less expressions. (right = 5)
Search for "random module" as "python random".
Score out of 100. Each question is 20 points.
Get the information from the user and each question is calculated based on the specified number of lives.
'''
import random

random_number = random.randint(1,50)
lives = 5
counter = 0
print("Welcome to the number guess game.")

while lives > 0:
    lives -= 1
    counter += 1
    guess = int(input("Choose a number between 1-50: "))
    if guess == random_number:
        print(f"Congrats, you guessed the number on the {counter}. try! Your point is {100- 20*(counter-1)}")
        break

    elif random_number > guess:
        print("The number is higher!")

    else:
        print("The number is lower!")

    if lives == 0:
        print(f"You do not have any lives left. The number is: {random_number}")
        break
