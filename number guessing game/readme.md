# Number Guessing Game 🎲

This is a beginner-friendly Python project where you try to guess a randomly generated number between 1 and 100. The game gives you hints to help you find the correct number.

## Features
- Generates a random number between 1 and 100.
- Gives hints to help you guess correctly:
  - Tells you if your guess is too high or too low.
- Counts the number of guesses you’ve made.
- Displays your total attempts once you guess the correct number.

## How to Play
1. When you run the game, you’ll be asked to guess a number.
2. The game will tell you if the guessed number is higher or lower than the target number.
3. Keep guessing until you find the correct number!
4. The game will show you the total attempts when you guess correctly.

## Code Explanation

Here's a quick look at how the code works:

```python
import random  # Imports the random library to generate a random number

# Generates a random number between 1 and 100
random_number = random.randint(1, 100)

# Takes the first guess from the user
guess_number = int(input("Guess a number: "))
guesses = 1  # Initializes the number of attempts

# Checks if the guessed number is correct
if random_number == guess_number:
    print("You guessed the correct number!")
else:
    # Loops until the correct number is guessed
    while random_number != guess_number:
        guesses += 1  # Counts each guess

        # Gives a hint if the guessed number is too high or too low
        if guess_number > random_number:
            print("Number is higher, please enter a lower number.")
            guess_number = int(input("Enter a lower number: "))
        elif guess_number < random_number:
            print("Number is lower, please enter a higher number.")
            guess_number = int(input("Enter a higher number: "))

# Displays the number of attempts taken to guess correctly
print(f"You guessed the correct number in {guesses} attempts!")
