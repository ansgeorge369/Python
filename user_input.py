"""
User Input in Python:
---------------------
- This script demonstrates **how to take user input** for different data types (string, integer, and float).
- The `input()` function is used to collect user input.
- `int()` is used to convert input into an **integer** (for age).
- `float()` is used to convert input into a **floating-point number** (for height).
- The collected information is displayed using `print()`.

Operations Demonstrated:
------------------------
1. **Taking string input** for the user's name.
2. **Taking integer input** for the user's age.
3. **Taking floating-point input** for the user's height.
4. **Displaying the collected data** using string concatenation.
"""

# Taking user input
name = input("Enter your name: ")  # Taking a string input

age = int(input("Enter your age: "))  # Taking an integer input for age

height = float(input("Enter your height in cm: "))  # Taking a float input for height

# Displaying the collected information
print("\nHello, " + name + "!")  
print("You are " + str(age) + " years old.")  
print("You are " + str(height) + " cm tall.")  
