"""
Temperature Check Program
-------------------------
This program asks the user to input the current outside temperature and 
provides feedback based on the temperature range.

- If the temperature is between 0°C and 40°C (inclusive), it's considered normal.
- If the temperature is below 0°C or above 40°C, it's considered harsh.

Logical Operators Used:
1. `and` - Ensures both conditions must be True.
2. `or` - Ensures at least one condition is True.
"""

# ------------ Taking User Input ------------
temp = int(input("What is the temperature outside (°C)? "))

# ------------ Checking Temperature Range ------------
if 0 <= temp <= 40:  # Checks if temperature is in the normal range
    print("Temperature is normal today.")
    print("Have a nice day! 😊")

elif temp < 0 or temp > 40:  # Checks if temperature is harsh
    print("Temperature is harsh today! ❄️🔥")
    print("Take necessary precautions! 🧥☀️")
