# This Python script defines two functions, hello() and hello2(), that print a greeting message 
# using a person's first, middle, and last name.
# 
# Key concepts covered:
# 1. **Function Definition**: Defining a function with parameters.
# 2. **String Concatenation**: Using `+` to combine strings.
# 3. **Positional Arguments**: Passing arguments in the same order as function parameters.
# 4. **Keyword Arguments**: Specifying arguments using parameter names, allowing flexibility in order.
#
# Use Cases:
# - This structure is useful when handling names in a formatted way (e.g., formal greetings, ID processing).
# - Using keyword arguments ensures clarity and prevents misplacement of values in function calls.

# Define the hello() function with three parameters: first, middle, and last
def hello(first, middle, last):
    # Print a greeting message with positional arguments.
    # Using `+` for string concatenation and `,` for separating values in the print function.
    print('Hello' + ' ' + first, middle, last)

# Call the hello() function using positional arguments (order matters)
hello('John', 'Smith', 'Doe')

# Define another function hello2() with the same parameters
def hello2(first, middle, last):
    # Similar to the previous function but demonstrating another way of concatenation
    print('Hello' + ' ' + first, middle, last)

# Call hello2() using keyword arguments (order can be changed)
hello2(last='Doe', first='John', middle='Smith')
