import random

print("Welcome to the Number Guessing Game!")
print("------------------------------------")

# Generate random number between 1 and 100
secret_number = random.randint(1, 100)

attempts = 0
guess = None

print("I have selected a number between 1 and 100.")
print("Try to guess it!\n")

while guess != secret_number:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess > secret_number:
        print("Too high! Try again.\n")
    elif guess < secret_number:
        print("Too low! Try again.\n")
    else:
        print("Congratulations! 🎉")
        print(f"You guessed the number in {attempts} attempts.")
        print("Thanks for playing!")