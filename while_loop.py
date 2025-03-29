"""
Looping Until a Valid Input is Provided:
----------------------------------------
- This script continuously prompts the user to **enter their name**.
- The `while` loop runs **as long as the input is empty** (`len(name) == 0`).
- Once the user enters a valid name, the loop exits and a greeting is displayed.

💡 Key Concepts Used:
- **`while` Loop**: Repeats execution until a condition is met.
- **`len()` Function**: Checks the length of a string.
- **String Concatenation**: Adds strings together using `+`.
"""

# Initialize an empty string
name = ""

# Run the loop until the user provides a valid input
while len(name) == 0:  # Equivalent to: while name == ""
    name = input("Enter your name: ")  # Take user input

# Display the greeting once input is provided
print("Hello " + name)
