"""
This script asks for the user's age and provides a message based on their eligibility to vote.

Conditions:
✔ If age is 100 → Suggests it's time to die (Dark humor, consider changing).
✔ If age is 18 or above → Eligible to vote.
✔ If age is negative → Asks for a valid age.
✔ Otherwise → Not eligible to vote.

"""

# Taking user input for age
age = int(input("Enter your age: "))
print("Your age is:", age)  # Displaying the entered age

# Checking conditions for age
if age == 100:
    print("It's time to die")  # Dark humor (Consider making this friendlier)
elif age >= 18:
    print("You are eligible to vote")  # Corrected the logic
elif age < 0:
    print("Enter a valid age")  # Handling negative ages
else:
    print("You are not eligible to vote")  # For ages below 18
