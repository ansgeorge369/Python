"""
Understanding **kwargs (Keyword Arguments)
------------------------------------------
- `**kwargs` allows us to pass a variable number of keyword arguments (key-value pairs) to a function.
- It is useful when we don't know beforehand how many keyword arguments will be passed.
"""

# ------------ Function with Normal Keyword Arguments ------------
def hello(first, last):
    """
    This function takes two keyword arguments (first and last name) 
    and prints a greeting message.
    """
    print('Hello', first, last)  

# Calling the function with named arguments
hello(first='John', last='Doe')  # Output: Hello John Doe


# ------------ Function with **kwargs (Arbitrary Keyword Arguments) ------------
def hi(**kwargs):
    """
    This function takes an arbitrary number of keyword arguments (**kwargs).
    It prints each keyword's value in a formatted greeting message.
    """
    print('Hi', end=' ')  # Print 'Hi' without a newline

    # Iterate through the keyword arguments and print their values
    for key, value in kwargs.items():
        print(value, end=' ')  

# Calling the function with multiple keyword arguments
hi(title='Mr', first='John', middle='Max', last='Doe')  # Output: Hi Mr John Max Doe
