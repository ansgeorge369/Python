"""
Understanding Variable Scope and the LEGB Rule in Python:
--------------------------------------------------------
- Python follows the **LEGB rule** to resolve variable names.
  - **L (Local scope)**: Variables declared inside a function.
  - **E (Enclosing scope)**: Variables in the outer function (used in nested functions).
  - **G (Global scope)**: Variables declared at the top level of the script.
  - **B (Built-in scope)**: Python's built-in functions and keywords.

This script demonstrates **variable scope** using a global variable and a function.

Key Concepts:
-------------
1. A global variable `name` is declared.
2. A function `display_name()` prints the `name` variable.
3. If a local variable **inside the function** is uncommented, it will override the global one.
4. The `name` variable is accessible both inside and outside the function due to Python's scope resolution.

"""

# Global Scope
name = 'Jose'  # This variable is accessible everywhere in the script

def display_name():
    # Local Scope (Uncomment the next line to see the effect of local scope)
    # name = 'Dante'  # This would override the global variable inside this function
    print(name)  # Python will search for 'name' following the LEGB rule

# Calling the function
display_name()  # This prints 'Jose' (or 'Dante' if the local variable is uncommented)

# Accessing the global variable
print(name)  # This prints 'Jose' because the global variable remains unchanged
