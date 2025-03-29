"""
This script demonstrates different types of `for` loops in Python.

Operations Performed:
1. Looping through a numeric range with a step size.
2. Looping through a numeric range with default step size.
3. Looping through a string (character iteration).
4. Countdown timer using `time.sleep()`.

Use Cases:
✔ Iterating through a sequence of numbers for mathematical computations.
✔ Looping through a string to process each character individually.
✔ Creating countdown timers, progress bars, or delays in automation scripts.
✔ Implementing repetitive tasks efficiently in Python.
"""

import time  # Importing time module to introduce delays in execution

# Looping through a range from 0 to 10 (excluding 10) with a step of 2
for i in range(0, 10, 2):
    print(i + 1)  # Adding 1 to each value before printing

# Looping through a range from 50 to 100 (inclusive)
for j in range(50, 100 + 1):
    print(j)  # Printing numbers from 50 to 100

# Looping through each character of the string "AnsGeorge"
for k in "AnsGeorge":
    print(k)  # Printing each character of the string separately

# Countdown timer from 10 to 1
for seconds in range(10, 0, -1):  # Start from 10, decrease by 1 each time
    print(seconds)  # Print the current countdown value
    time.sleep(1)  # Pause execution for 1 second to create a real-time countdown

print("Blast Off!")  # Display final message after countdown
