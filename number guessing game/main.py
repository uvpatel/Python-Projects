import random

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)

# Take the player's first guess
guess_number = int(input("Guess a number: "))
guesses = 1    

# Check if the first guess is correct
if random_number == guess_number:
    print("You guessed the correct number!")
else:
    # Loop until the correct number is guessed
    while random_number != guess_number:
        guesses += 1  # Increase guess count

        # Provide hints
        if guess_number > random_number:
            print("Number is higher, please enter a lower number.")
            guess_number = int(input("Enter a lower number: "))
        elif guess_number < random_number:
            print("Number is lower, please enter a higher number.")
            guess_number = int(input("Enter a higher number: "))

# Final message with the number of attempts
print(f"You guessed the correct number in {guesses} attempts!")
