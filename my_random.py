"""
Random Module Demonstration
---------------------------
This script demonstrates the use of Python's `random` module to generate random numbers,
select random elements from a list, and shuffle a list.

Key Features:
1. Generates a random integer between 1 and 100.
2. Generates a random floating-point number between 0 and 1.
3. Selects a random choice from a predefined list.
4. Shuffles a deck of cards.

Functions Used:
- `random.randint(a, b)`: Returns a random integer between `a` and `b` (inclusive).
- `random.random()`: Returns a random float between `0.0` and `1.0`.
- `random.choice(sequence)`: Returns a random element from a non-empty sequence.
- `random.shuffle(sequence)`: Shuffles a list in place.
"""

import random  # Importing the random module

# Generate a random integer between 1 and 100
x = random.randint(1, 100)
print(f"🎲 Random Integer: {x}")

# Generate a random floating-point number between 0 and 1
y = random.random()
print(f"🔢 Random Float: {y:.4f}")  # Display up to 4 decimal places

# Random selection from a list
choices = ['rock', 'paper', 'scissors']
selected_choice = random.choice(choices)
print(f"🖐️ Random Choice: {selected_choice}")

# Deck of playing cards
cards = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']

# Shuffle the deck
random.shuffle(cards)
print(f"🃏 Shuffled Deck: {cards}")
