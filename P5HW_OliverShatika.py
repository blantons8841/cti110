# Shatika Oliver
# May 2, 2025
# P5HW 
# This program generates a random number between 1 and 100 and lets the user guess until they find it.
# The program tracks the number of attempts and gives feedback if the guess is too high or too low.

import random

def get_user_guess():
    guess = int(input("Enter your guess (1-100): "))
    while guess < 1 or guess > 100:
        print("Invalid input. Please enter a number between 1 and 100.")
        guess = int(input("Enter your guess (1-100): "))
    return guess

def play_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guess = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100...")

    while guess != number_to_guess:
        guess = get_user_guess()
        attempts += 1

        if guess < number_to_guess:
            print("Too low. Try again.")
        elif guess > number_to_guess:
            print("Too high. Try again.")

    print(f"Congratulations! You guessed the number in {attempts} attempts.")

def main():
    play_again = "yes"
    while play_again == "yes":
        play_guessing_game()
        play_again = input("Would you like to play again? (yes/no): ").strip().lower()
        while play_again not in ["yes", "no"]:
            play_again = input("Please enter 'yes' or 'no': ").strip().lower()

    print("Thanks for playing!")

main()
