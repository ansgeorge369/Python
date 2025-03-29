"""
Mathematical Operations in Python using `math` Module
------------------------------------------------------
This script demonstrates various mathematical functions such as:
- Rounding (round, ceil, floor)
- Absolute value
- Power and square root calculations
- Maximum, minimum, sum, and average calculations
- Modulus, integer division, and exponentiation

The `math` module is used to enhance mathematical capabilities.
"""

import math  # Importing the math module for advanced mathematical functions

# Defining variables
pi = 3.14  # Approximate value of π
x, y, z = 1, 2, 3  # Example numbers

# -------- Rounding Operations --------
print("Rounded π:", round(pi))  # Rounds to the nearest integer (3)
print("Ceil of π:", math.ceil(pi))  # Rounds up (4)
print("Floor of π:", math.floor(pi))  # Rounds down (3)

# -------- Absolute Value --------
print("Absolute value of -pi:", abs(-pi))  # Returns 3.14 (removes negative sign)

# -------- Power and Square Root --------
print("2^3:", pow(2, 3))  # 2 raised to the power 3 (2³ = 8)
print("Square root of 25:", math.sqrt(25))  # √25 = 5.0

# -------- Finding Maximum, Minimum, and Sum --------
print("Maximum of (x, y, z):", max(x, y, z))  # Finds the largest number (3)
print("Minimum of (x, y, z):", min(x, y, z))  # Finds the smallest number (1)
print("Sum of (x, y, z):", sum((x, y, z)))  # Sums up all values (1 + 2 + 3 = 6)

# -------- Average and Modulus Calculations --------
total = sum((x, y, z))  # Storing sum for reuse
print("Average:", total / 3)  # Regular division to get the average (6 / 3 = 2.0)
print("Integer division (floor of average):", total // 3)  # Integer division (6 // 3 = 2)
print("Modulus (remainder when sum is divided by 3):", total % 3)  # 6 % 3 = 0

# -------- Exponentiation --------
print("Sum raised to power 3:", total ** 3)  # 6³ = 216
print("Cube root of sum:", total ** (1/3))  # Cube root of 6 ≈ 1.817

