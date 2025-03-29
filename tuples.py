"""
Tuples in Python:
------------------
- **Tuples** are ordered, immutable collections used to store multiple items in a single variable.
- **Immutable** means that once a tuple is created, its elements cannot be changed, added, or removed.
- Tuples are **faster than lists** due to their immutability, making them ideal for read-only data.

Operations Demonstrated:
-------------------------
1. **Counting elements** in a tuple using `count()`.
2. **Finding the index** of an element using `index()`.
3. **Iterating** over a tuple with a `for` loop.
4. **Checking for membership** using `if...in` statements.
"""

# Creating a tuple
student = ("Dante", "15", "Male")

# Counting occurrences of an element in a tuple
print("Count of '15':", student.count("15"))  # Output: 1

# Finding the index of an element in a tuple
print("Index of 'Male':", student.index("Male"))  # Output: 2

# Iterating through the tuple using a for loop
print("\nStudent Details:")
for i in student:
    print(i)

# Checking if an element exists in the tuple
if "Dante" in student:
    print("\nDante is in the list")
else:
    print("\nDante is not in the list")
