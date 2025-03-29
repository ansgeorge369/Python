"""
This script demonstrates various formatting techniques in Python using `str.format()`.

Operations Performed:
1. Basic string concatenation and formatting.
2. Positional and keyword arguments in `.format()`.
3. Formatting text with padding (left, right, and center alignment).
4. Formatting numbers with decimal precision, thousands separator, and different numeral systems.

Use Cases:
✔ Creating well-structured and readable output strings.
✔ Aligning and padding text for better formatting.
✔ Formatting numbers in different representations (binary, octal, hex, scientific notation).
✔ Precision control for floating-point numbers.
"""

# Defining variables
animal = 'Dog'
item = 'wall'

# String concatenation using `+`
print('The ' + animal + ' ran away from the ' + item + '.')

# Using positional arguments in `format()`
print('The {0} ran away from the {1}.'.format(animal, item))  # Correct positional order
print('The {1} ran away from the {1}.'.format(animal, item))  # Using same index twice

# Using keyword arguments in `format()`
print('The {vehicle} ran through the {place}.'.format(vehicle='car', place='park'))  # Correct usage
print('The {vehicle} ran through the {vehicle}.'.format(vehicle='car', place='park'))  # Repeating the same variable

# Storing format string in a variable and applying formatting later
text = 'The {0} ran away from the {1}.'
print(text.format(animal, item))

# ---- TEXT ALIGNMENT AND PADDING ----

name = 'Doe'
print('Hello my name is {}'.format(name))  # Basic string formatting

# Left align within 10-character width
print('Hello my name is {:10}. Nice to meet you'.format(name))

# Right align within 10-character width
print('Hello my name is {:>10}. Nice to meet you'.format(name))

# Center align within 10-character width
print('Hello my name is {:^10}. Nice to meet you'.format(name))

# ---- NUMBER FORMATTING ----

num = 3.14159
print('The number pi is {:.2f}'.format(num))  # Rounds to 2 decimal places
print('The number pi is {:.3f}'.format(num))  # Rounds to 3 decimal places

num2 = 987456
print('The number is {:,}'.format(num2))  # Adds comma as a thousands separator
print('The number is {:b}'.format(num2))  # Converts number to binary format
print('The number is {:o}'.format(num2))  # Converts number to octal format
print('The number is {:X}'.format(num2))  # Converts number to uppercase hexadecimal format
print('The number is {:E}'.format(num2))  # Converts number to scientific notation
