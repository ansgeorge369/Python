"""
This script demonstrates the use of dictionaries in Python. A dictionary is:
✔ A mutable (changeable) collection.
✔ Unordered, meaning elements are not stored in a specific order.
✔ A key-value pair structure, where keys must be unique.
✔ Optimized for fast access using hash tables.

Operations performed in this script:
1. Creating a dictionary of country capitals.
2. Updating the dictionary by adding new key-value pairs.
3. Modifying an existing key-value pair.
4. Removing a key-value pair.
5. Retrieving values using both direct indexing and the `get()` method.
6. Fetching all keys, values, and key-value pairs.
7. Iterating over the dictionary to print all key-value pairs.
8. Clearing the entire dictionary.

Use Cases:
✔ Storing and retrieving large datasets efficiently.
✔ Fast lookups due to hashing.
✔ Organizing data in a structured format (e.g., database-like storage).
"""

# Creating a dictionary with country names as keys and their capitals as values
capitals = {'France': 'Paris', 
            'Germany': 'Berlin', 
            'Japan': 'Tokyo', 
            'Italy': 'Rome', 
            'Spain': 'Madrid', 
            'USA': 'Washington DC'}

# Adding a new key-value pair to the dictionary
capitals.update({'India': 'New Delhi'})

# Updating an existing key (USA) with a new value ('LA')
capitals.update({'USA': 'LA'})

# Removing the 'USA' entry from the dictionary
capitals.pop('USA')

# Accessing the capital of France using direct indexing
print(capitals['France'])  

# Trying to access 'India' using direct indexing would raise a KeyError if the key does not exist
# print(capitals['India'])  # Uncommenting this line may cause an error if 'India' is not in the dictionary

# Using .get() method to retrieve the value of 'India', returns `None` if the key is missing
print(capitals.get('India'))  

# Printing all keys in the dictionary
print(capitals.keys())  

# Printing all values in the dictionary
print(capitals.values())  

# Printing all key-value pairs as tuples in a list
print(capitals.items())  

# Iterating through the dictionary and printing each key-value pair
for key, value in capitals.items():
    print(key, value)

# Clearing all entries from the dictionary
capitals.clear()  
