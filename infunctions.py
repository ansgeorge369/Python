"""
Multiple Assignment & String Methods in Python
----------------------------------------------
This script demonstrates:
1. **Multiple assignment** - Assigning values to multiple variables in a single line.
2. **String methods** - Various built-in functions to manipulate and analyze strings.
"""

# ----------- Multiple Assignment -----------
# Assigning values to multiple variables in a single line
name, age, height = "Ans", 25, 170  # `name` is a string, `age` is an integer, `height` is an integer
print(name, age, height)  # Output: Ans 25 170

# Assigning the same value to multiple variables
Kenshin = Santa = Lee = Bridge = 30  # All variables will hold the value 30
print(Kenshin, Santa, Lee, Bridge)  # Output: 30 30 30 30

# ----------- String Methods -----------
name2 = "AnsGeorge"

# Get the length of the string
print(len(name2))  # Output: 9 (Counts total characters including uppercase and lowercase)

# Convert the string to lowercase
print(name2.lower())  # Output: ansgeorge

# Convert the string to uppercase
print(name2.upper())  # Output: ANSGEORGE

# Capitalize the first letter of each word
print(name2.title())  # Output: Ansgeorge

# Find the index of the first occurrence of a character
print(name2.find("o"))  # Output: 5 (Index starts at 0, so 'o' is at position 5)

# Capitalize only the first letter of the string
print(name2.capitalize())  # Output: Ansgeorge

# Check if the string contains only digits
print(name2.isdigit())  # Output: False (Because it contains letters)

# Check if the string contains only alphabets
print(name2.isalpha())  # Output: True (No numbers or special characters)

# Count occurrences of a specific character
print(name2.count("r"))  # Output: 1 (Only one occurrence of 'r')

# Replace a character with another character
print(name2.replace("o", "a"))  # Output: AnsGearge (Replaces 'o' with 'a')

# Print the string multiple times
print(name2 * 3)  # Output: AnsGeorgeAnsGeorgeAnsGeorge
