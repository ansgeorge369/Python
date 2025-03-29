# This Python script demonstrates the concept of return values in functions.
# Functions can send values or objects back to the caller using the `return` statement.
# The returned values can then be stored in variables or used directly in expressions.
#
# Key concepts covered:
# 1. **Function Return Values**: Functions returning computed results.
# 2. **Multiplication & Addition Operations**: Basic arithmetic operations inside functions.
# 3. **Storing Return Values**: Assigning function results to variables.
# 4. **Printing Results**: Displaying returned values using `print()`.
#
# Use Cases:
# - Used in **mathematical computations** where reusable logic is needed.
# - Helps in **modular programming** by breaking down tasks into functions.
# - Essential for **returning processed data** in real-world applications.

# Define a function multiply() that takes two arguments x and y
def multiply(x, y):
    # Compute the product of x and y
    result = x * y
    # Return the computed product back to the caller
    return result

# Call the multiply function with arguments 2 and 3
# The return value (6) is assigned to variable x
x = multiply(2, 3)

# Print the result of multiplication
print(x)  # Output: 6

# Define a function add() that takes two arguments x and y
def add(x, y):
    # Compute the sum of x and y and return it directly
    return x + y

# Call the add function with arguments 2 and 3
# The return value (5) is assigned to variable x
x = add(2, 3)

# Print the result of addition
print(x)  # Output: 5
