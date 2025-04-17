import random
def guess_number():
    """Play a number guessing game, return attempts."""
    secret = random.randint(1, 10)
    attempts = 0
    while True:
        try:
            guess = int(input("Guess a number (1-10): "))
            attempts += 1
            if guess == secret:
                return attempts
            elif guess < secret:
                print("Too low")
            else:
                print("Too high")
        except ValueError:
            print("Enter a valid number")
result = guess_number()
print(f"You won in {result} attempts!")