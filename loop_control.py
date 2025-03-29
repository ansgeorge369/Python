"""
Loop Control Statements in Python
----------------------------------
This script demonstrates the use of `break`, `continue`, and `pass` statements
in different scenarios.

1. `break` - Exits a loop when a condition is met.
2. `continue` - Skips the current iteration and moves to the next.
3. `pass` - Acts as a placeholder (does nothing).
"""

# ------------ Using `break` to Exit Loop ------------
while True:
    name = input("Enter your name: ")  # Taking user input
    if name.strip() != "":  # Ensuring input isn't empty (strip removes extra spaces)
        break  # Exit loop when a valid name is entered

# ------------ Using `continue` to Skip Characters ------------
phone_number = "123-456-7890"
print("\nFiltered Phone Number (without '-'): ", end="")

for i in phone_number:
    if i == "-":  # Skipping dashes
        continue
    print(i, end="")  # Printing numbers without dashes

# ------------ Using `pass` as a Placeholder ------------
print("\n\nPrinting numbers from 0 to 30 (Skipping 13):")

for j in range(0, 31):
    if j == 13:  # Placeholder for a condition that will be handled later
        pass  # Does nothing, just a placeholder
    else:
        print(j)
