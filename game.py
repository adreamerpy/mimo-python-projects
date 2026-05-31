import random

print("--- Welcome to the Number Guessing Game! ---")
secret_number = random.randint(1, 50)
print("I am thinking of a number between 1 and 50. Can you guess it?")

while True:
    try:
        guess = int(input("Enter your guess: "))
        if guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print("Wow! Congratulations! You guessed the number.")
            break
    except ValueError:
        print("Please enter a valid number!")