"""
Sets in Python:
----------------
- A **set** is an unordered and unindexed collection of unique elements.
- **Duplicate values are not allowed** in sets.
- Sets are useful when you need a **collection of unique items**.

Operations Demonstrated:
-------------------------
1. Creating a set with duplicate values (they are automatically removed).
2. Adding an element to the set.
3. Removing an element from the set.
4. Clearing all elements from the set.
5. Updating a set by adding elements from another set.

"""

# Creating a set (duplicates will be removed automatically)
utensils = {"fork", "spoon", "knife", "fork", "spoon"}
print("Initial set of utensils:", utensils)  # Output: {'fork', 'knife', 'spoon'}

# Creating another set
dishes = {"plate", "bowl", "cup"}

# Adding an element to the set
utensils.add("napkin")
print("After adding 'napkin':", utensils)  # Output includes 'napkin'

# Removing an element from the set
utensils.remove("spoon")  
print("After removing 'spoon':", utensils)  # Output no longer includes 'spoon'

# Clearing all elements from the set
utensils.clear()
print("After clearing utensils:", utensils)  # Output: set()

# Updating the set by adding elements from another set
utensils.update(dishes)
print("After updating utensils with dishes:", utensils)  # Output includes 'plate', 'bowl', 'cup'
