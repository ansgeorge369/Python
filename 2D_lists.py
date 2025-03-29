# This Python script demonstrates the concept of a 2D list (nested list).
# A 2D list is a list containing other lists as its elements.
# It allows structured storage of data, similar to a table or a matrix.
#
# Key concepts covered:
# 1. **Nested Lists (2D Lists)**: Lists within a list to organize related data.
# 2. **Indexing in 2D Lists**: Accessing elements using row and column indexes.
# 3. **Printing Nested Lists**: Understanding list structures via print statements.
#
# Use Cases:
# - Useful for **representing structured data** like menus, tables, or matrices.
# - Helps in **grouping related items** logically for easy access.
# - Commonly used in **game development**, **data analysis**, and **machine learning** for storing grid-like data.

# Define a list of drinks
drinks = ["coffe", "soda", "tea"]

# Define a list of dinner items
dinner = ["Biriyani", "Porotta", "Mandhi"]

# Define a list of desserts
desserts = ["Ice cream", "Cake", "Pizza"]

# Create a 2D list (nested list) by combining all three lists
food = [drinks, dinner, desserts]

# Print the entire 2D list
print(food)  # Output: [['coffe', 'soda', 'tea'], ['Biriyani', 'Porotta', 'Mandhi'], ['Ice cream', 'Cake', 'Pizza']]

# Access and print the second list (dinner) using its index (1)
print(food[1])  # Output: ['Biriyani', 'Porotta', 'Mandhi']

# Access and print the second item of the dinner list using row and column indexes
print(food[1][1])  # Output: 'Porotta'
