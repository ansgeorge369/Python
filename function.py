"""
This script defines and demonstrates the use of functions in Python.

Features:
✔ `hello(name)`: Greets the user with their name.
✔ `welcome(name1, name2, age)`: Welcomes the user with their full name and age.
✔ Uses user input to collect name and age before calling the functions.

Use Cases:
✔ Avoids repetition by using functions for reusable code.
✔ Demonstrates how to pass and use parameters in functions.
✔ Encourages better code structure and readability.
"""

# Function to greet the user
def hello(name):
    """Prints a simple greeting using the given name."""
    print("Hello " + name)
    print("Hello Again")

# Function to welcome the user with first name, last name, and age
def welcome(name1, name2, age):
    """Prints a welcome message including first name, last name, and age."""
    print("Welcome " + name1 + " " + name2)  # Concatenating first and last name
    print("Welcome Again")
    print("Your age is " + str(age))  # Converting age to string before concatenation

# Taking user input for the first function
my_name = input("What is your name? ")
hello(my_name)  # Calling hello function with user input

# Taking user input for the second function
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
age = int(input("What is your age? "))  # Converting input to integer

welcome(first_name, last_name, age)  # Calling welcome function with user input
