# This Python script implements a simple Rock-Paper-Scissors game.
# The player competes against the computer, which randomly selects a move.
# The game follows standard Rock-Paper-Scissors rules:
# - Rock beats Scissors
# - Scissors beat Paper
# - Paper beats Rock
#
# Key concepts covered:
# 1. **Random Selection**: The computer's choice is selected using `random.choice()`.
# 2. **Dictionary for Game Rules**: The rules are stored in a dictionary for easy lookup.
# 3. **Function-Based Structure**: Uses functions for modularity and better code organization.
# 4. **User Input Handling**: Ensures valid input and allows replaying the game.
# 5. **Looping for Continuous Play**: The game continues until the user decides to stop.
#
# Use Cases:
# - A fun way to practice **conditional logic** and **looping** in Python.
# - Can be expanded into a **GUI version** using Tkinter or Pygame.
# - Useful for **learning basic game development concepts**.

# Import the random module for generating the computer's choice
import random

# Function to determine the winner between the player and the computer
def get_winner(player, computer):
    # Dictionary defining the game rules: key beats value
    rules = {
        'rock': 'scissors',   # Rock beats Scissors
        'scissors': 'paper',  # Scissors beat Paper
        'paper': 'rock'       # Paper beats Rock
    }

    # If both player and computer choose the same, it's a tie
    if player == computer:
        return "It's a Tie!"
    
    # If the player's choice beats the computer's choice based on rules, the player wins
    elif rules[player] == computer:
        return "Player wins!"
    
    # Otherwise, the computer wins
    else:
        return "Computer wins!"

# Function to handle the gameplay loop
def play_game():
    # List of valid choices for both player and computer
    choices = ['rock', 'paper', 'scissors']

    # Infinite loop to allow replaying the game until the user exits
    while True:
        # Computer randomly selects one of the choices
        computer = random.choice(choices)

        # Initialize player choice as None
        player = None

        # Loop until the player enters a valid choice
        while player not in choices:
            player = input("\nChoose rock, paper, or scissors: ").lower()

        # Display choices made by both computer and player
        print(f"\n🖥️ Computer chose: {computer}")
        print(f"🙋 Player chose: {player}")

        # Determine and print the result using the get_winner() function
        print("🏆 Result:", get_winner(player, computer))

        # Ask the user if they want to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()

        # If the user does not enter 'yes', exit the game loop
        if play_again != 'yes':
            print("\nThanks for playing! Goodbye! 👋")
            break

# Start the game
play_game()
