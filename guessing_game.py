# Guess My Number

import random

print("\tWelcome to the Number Guessing Game!")
print("\n\nI'm thinking of a number between 1 and 100")
print("Try to guess it in as few attempts as possible.\n\n")

number = random.randint(1, 100)
guess = int(input("Take a guess: "))
tries = 1

while guess != number:
    if guess > number:
        print("Lower... ")
    else:
        print("Higher... ")

    guess = int(input("Take a guess: "))
    tries += 1

print("\n\nCongratulations, you guessed it! The number was", number)
print("It took you", tries, "tries to guess correctly.")

input("\n\nPress the enter key to exit.")


