"""
Module Import Example
---------------------
This script imports a custom module named 'messages' (saved as messages.py).
It contains two functions:
1. `hello()`: Prints a greeting message.
2. `bye()`: Prints a farewell message.

There are two ways to import modules:
1. `import module_name as alias` → Call functions using `alias.function_name()`.
2. `from module_name import function1, function2` → Call functions directly.

The `help('modules')` command lists all available modules in the Python environment.
"""

# Importing the 'messages' module with an alias
import messages as msg

# Calling functions from the imported module
msg.hello()
msg.bye()

# Alternative way to import specific functions (commented)
# from messages import hello, bye
# hello()
# bye() 

# Displaying available Python modules
help('modules')
