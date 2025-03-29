"""
This script demonstrates the use of the index operator `[]` to access elements 
in a string. It includes case conversion, string slicing, and error handling.

Features:
✔ Checks if the first letter of the name is 'A' (case-insensitive).
✔ Converts the name to uppercase if the first letter is lowercase.
✔ Extracts the first name (first three letters).
✔ Extracts the last name by handling spaces and avoiding errors.
✔ Retrieves the last character of the string.
✔ Ensures the script does not crash if the input is empty.

Use Cases:
✅ Useful for name formatting in user registration.
✅ Can be adapted for username validation in applications.
✅ Demonstrates error handling for robust string operations.
"""

# Defining a sample name
name = "ans George !"  # Example input

# Ensure the string is not empty before checking the first character
if name and name[0].upper() == 'A':  
    print("Hello Mr. Ans")  # Greeting if the first letter is 'A'
else:
    print("Hello Mr. George")  # Default greeting

# Convert name to uppercase if the first letter is lowercase
if name and name[0].islower():
    name = name.upper()  # Convert the whole name to uppercase

print("Updated Name:", name)  # Display the modified name

# Extracting first name (first 3 letters)
first_name = name[0:3].upper()  # Extracts first 3 characters and converts to uppercase
print("First Name:", first_name)

# Extracting last name (from index 4 to the end), handling cases where name might be short
# Using split() to safely get the last name, avoiding index errors
name_parts = name.split()  # Splitting name into parts based on spaces
last_name = name_parts[1].lower() if len(name_parts) > 1 else "N/A"  # Get second word if available
print("Last Name:", last_name)

# Extracting the last character of the string
last_character = name[-1] if name else "N/A"  # Ensures it works even if the string is empty
print("Last Character:", last_character)
