"""
Understanding Lists in Python
-----------------------------
- Lists are **ordered**, **mutable**, and **allow duplicate values**.
- They can hold different data types and support various operations such as insertion, deletion, sorting, and iteration.
"""

# ------------ Creating a List ------------
food = ["rice", "noodles", "porotta", "Dosa"]  # A list of food items

# ------------ Modifying Elements in the List ------------
food[3] = "Pizza"  # Changing the fourth element ("Dosa") to "Pizza"
print(food[3])  # Output: Pizza

# ------------ Adding Elements to the List ------------
food.append("ice cream")  # Appends "ice cream" to the end of the list

# ------------ Removing Elements from the List ------------
food.remove("noodles")  # Removes "noodles" from the list

# ------------ Removing Last Element (Using pop) ------------
food.pop()  # Removes the last item in the list (i.e., "ice cream")

# ------------ Inserting an Element at a Specific Index ------------
food.insert(2, "Pasta")  # Inserts "Pasta" at index 2 (third position)

# ------------ Sorting the List in Ascending Order ------------
food.sort()  # Sorts the list alphabetically

# ------------ Clearing the List ------------
food.clear()  # Removes all elements from the list

# ------------ Iterating Over the List ------------
for i in food:
    print(i)  # Prints each item in the list
