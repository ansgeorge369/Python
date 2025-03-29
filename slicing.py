"""
String Slicing and Manipulation in Python:
-------------------------------------------
- **String slicing** allows you to extract specific parts of a string using the `[:]` operator.
- **Syntax:** `string[start:end:step]`
- **Negative indexing** allows reverse traversal of a string.
- The `slice()` function can also be used for string slicing.

Operations Demonstrated:
-------------------------
1. Extracting the first name from a full name.
2. Extracting the last name.
3. Using a step value to extract alternate characters.
4. Reversing a string using negative step values.
5. Using `slice()` function to extract domain names from URLs.
"""

# Defining a string
name = "Ans George"

# Extracting the first name (from index 0 to 3)
first_name = name[:3]   # "Ans"

# Extracting the last name (from index 4 to the end)
last_name = name[4:]    # "George"

# Extracting every second character from the string
test_name = name[::2]   # "AsGog"

# Reversing the string using a negative step value
reversed_name = name[::-1]  # "egroG snA"

# Printing results
print("First Name:", first_name)
print("Last Name:", last_name)
print("Every second character:", test_name)
print("Reversed Name:", reversed_name)

# Working with URLs using the slice() function
website1 = "http://www.google.com"
website2 = "http://www.yahoo.com"
website3 = "http://www.bing.com"

# Creating a slice object to extract domain names (excluding "http://www." and ".com")
slice_func = slice(7, -4)

# Extracting and printing domain names
print("Extracted domain from website1:", website1[slice_func])  # google
print("Extracted domain from website2:", website2[slice_func])  # yahoo
print("Extracted domain from website3:", website3[slice_func])  # bing
