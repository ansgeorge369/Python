# Calculate sum and average in a loop
total = 0
for i in range(1, 4):  # 1, 2, 3
    total += i         # += is shorthand for total = total + i
average = total / 3
print(f"Sum: {total}, Average: {average}")  # Output: Sum: 6, Average: 2.0