def print_number_pattern(n):
    for i in range(1, n + 1):  # Outer loop for rows
        for j in range(i):     # Inner loop for printing i, i times
            print(i, end=" ")
        print()  # New line after each row

# Get input from user
try:
    n = int(input("Enter a positive integer: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        print_number_pattern(n)
except ValueError:
    print("Invalid input. Please enter a valid integer.")

# User Input:
# input("Enter a positive integer: ") prompts the user to enter a number.
# int() converts the input string to an integer.
# A try-except block handles invalid inputs (e.g., non-integer values like "abc").
# A check ensures n is positive; if not, an error message is printed.
# Program Flow:
# If the input is valid and positive, print_number_pattern(n) is called.
# The function uses nested loops:
# Outer loop: Iterates from 1 to n for rows.
# Inner loop: Prints i (row number) i times per row.
# print() adds a newline after each row.
# Data Flow:
# User input n determines the number of rows.
# Variable i controls the row number and value printed.
# Output is printed directly, no storage needed. 