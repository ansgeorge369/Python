# This Python script takes a numerical input from the user, processes it, and prints the final rounded absolute value.
# It demonstrates the concept of nested function calls, where multiple functions are executed in a single line.
# The script has two parts:
# 1. A step-by-step approach using separate variable assignments.
# 2. A compact, single-line version that achieves the same result using nested functions.

# Prompt the user to enter a number as input (input is received as a string)
num = input("Enter the number: ")

# Convert the input string to a floating-point number
num = float(num)

# Get the absolute value of the number (removes negative sign if any)
num = abs(num)

# Round the number to the nearest integer
num = round(num)

# Print the final rounded absolute value
print(num)

# Single-line version:
# This line demonstrates nested function calls.
# The execution order follows an inside-out approach:
# 1. input('Enter a number: ') - Takes user input as a string.
# 2. float(...) - Converts the string to a floating-point number.
# 3. abs(...) - Takes the absolute value of the number.
# 4. round(...) - Rounds the number to the nearest integer.
# 5. print(...) - Prints the final result.
print(round(abs(float(input('Enter a number: ')))))  
