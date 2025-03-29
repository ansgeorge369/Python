# This Python script demonstrates the use of *args in functions.
# *args allows a function to accept a variable number of positional arguments.
# It packs all arguments into a tuple, making it flexible for different numbers of inputs.
#
# Key concepts covered:
# 1. **Positional Arguments**: Fixed parameters in functions.
# 2. **Using *args**: Allowing a function to take multiple arguments dynamically.
# 3. **Tuple to List Conversion**: Modifying arguments by converting a tuple to a list.
# 4. **Iterating Over *args**: Using a loop to process all arguments.
#
# Use Cases:
# - Useful when the number of function arguments is **not predetermined** (e.g., sum of numbers).
# - Helps in **dynamic calculations** like processing user inputs or handling lists of values.
# - Commonly used in **mathematical functions, logging frameworks, and API handling**.

# Define a function add() that takes two fixed arguments
def add(num1, num2):
    # Compute the sum of num1 and num2
    result = num1 + num2
    # Return the computed sum
    return result

# Call the add() function with two arguments and print the result
print(add(10, 20))  # Output: 30

# Define a function add2() that can take multiple arguments using *args
def add2(*args):
    # Initialize sum variable to store the result
    sum = 0

    # Convert args tuple to a list to allow modification
    args = list(args)

    # Modify the second element (index 1) of the list to 10
    args[1] = 10

    # Iterate through each value in the modified args list
    for i in args:
        # Add each number to sum
        sum += i

    # Return the final sum
    return sum

# Call add2() with multiple arguments and print the result
print(add2(1, 2, 3, 4, 5))  # Output: 1 + 10 + 3 + 4 + 5 = 23
