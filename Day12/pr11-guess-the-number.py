# Guess the number game
import random
from art import logo

print(logo)

def guess_the_number():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number_to_guess = random.randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    attempts = 10 if difficulty == "easy" else 5
    print(f"You have {attempts} attempts remaining to guess the number.")

    while attempts > 0:
        guess = int(input("Make a guess: "))

        if guess == number_to_guess:
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts!")
            return
        elif guess < number_to_guess:
            print("Too low.")
        else:
            print("Too high.")

        attempts -= 1
        print(f"You have {attempts} attempts remaining to guess the number.")

    print(f"You've run out of guesses, you lose. The number was {number_to_guess}.")

guess_the_number()