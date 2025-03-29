"""
Understanding Variables and Data Types in Python:
-------------------------------------------------
- Python automatically assigns a **data type** to variables.
- The primary data types used here are:
  1. **String (`str`)**: Used for text.
  2. **Integer (`int`)**: Used for whole numbers.
  3. **Float (`float`)**: Used for decimal numbers.
  4. **Boolean (`bool`)**: Used for True/False values.

This script demonstrates:
- Assigning values to variables.
- Concatenating strings.
- Performing arithmetic operations on integers.
- Converting data types for proper output formatting.
- Checking the type of each variable using `type()`.
"""

# String Variables
first_name = "Ans"   # Assigning a string value
last_name = "George" # Assigning another string value

# String Concatenation
full_name = first_name + " " + last_name  # Combining first and last name with a space
print("Your name is " + full_name)  # Output: Your name is Ans George
print(type(full_name))  # Checking the data type (str)

# Integer Variables
age = 25  # Assigning an integer value
age += 1  # Incrementing the value of age by 1
print("And your age is " + str(age))  # Output: And your age is 26
print(type(age))  # Checking the data type (int)

# Float Variables
height = 180.80  # Assigning a floating-point value
print("Your height is " + str(height) + "cm")  # Output: Your height is 180.8cm
print(type(height))  # Checking the data type (float)

# Boolean Variable
human = True  # Assigning a boolean value
print("Are you a human? " + str(human))  # Output: Are you a human? True
print(type(human))  # Checking the data type (bool)
