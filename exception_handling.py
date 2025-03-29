"""
This script demonstrates exception handling in Python using try-except blocks.
It safely handles user input and prevents the program from crashing due to errors.

Operations performed:
1. Accepting a numerator and denominator from the user.
2. Performing division while handling possible errors.
3. Using multiple except blocks to handle:
   ✔ `ZeroDivisionError`: Prevents division by zero.
   ✔ `ValueError`: Handles non-integer input.
   ✔ `Exception`: Catches any other unexpected errors.
4. Using an `else` block to execute code when no exceptions occur.
5. Using a `finally` block to execute code regardless of an exception occurring.

Use Cases:
✔ Ensuring a program doesn't crash due to user errors.
✔ Handling input validation gracefully.
✔ Providing meaningful error messages to the user.
✔ Running cleanup tasks (if needed) in the `finally` block.
"""

try:
    # Taking input for the numerator and converting it to an integer
    numerator = int(input("Enter numerator: "))

    # Taking input for the denominator and converting it to an integer
    denominator = int(input("Enter denominator: "))

    # Performing division operation
    result = numerator / denominator

# Handling division by zero error
except ZeroDivisionError as e:
    print(e)  # Printing the built-in error message
    print("Denominator can't be zero")  # Custom error message for clarity

# Handling invalid input (if the user enters a non-integer value)
except ValueError as e:
    print(e)  # Printing the built-in error message
    print("Invalid input")  # Custom error message

# Handling any other unexpected exceptions
except Exception as e:
    print(e)  # Printing the built-in error message
    print("Something went wrong :(")  # Generic error message

# Executed only if no exceptions occur
else:
    print(result)  # Printing the result of the division

# Executed regardless of whether an exception occurs or not
finally:
    print("This will always run")  # Indicating the end of the try-except block
