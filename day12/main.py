import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)
# print(f"number is {number}")
difficultly = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = 0
correct_guess = False
if difficultly == "easy":
    print("Easy")
    attempts = 10
elif difficultly == "hard":
    print("Hard")
    attempts = 5
else:
    print("Bye")

while attempts > 0 and not correct_guess:
    print(f"You have {attempts} remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == number:
        correct_guess = True
        break
    elif guess < number:
        print("Too low.")
    elif guess > number:
        print("Too high.")
    attempts -= 1
    if attempts > 1:
        print("Guess again.")


if correct_guess:
    print(f"You got it! The answer was {number}")
else:
    print("You've run out of guesses, you lose.")
