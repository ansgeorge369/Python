"""
This program prints a rectangle of symbols using nested loops.

Concept:
---------
- The outer loop controls the number of rows.
- The inner loop controls the number of columns and prints the symbols.
- Since the inner loop runs completely for each iteration of the outer loop, 
  this is an example of **nested loops**.

Example Execution:
-------------------
Input:
How many Rows? : 3
How many Columns? : 5
What symbol do you want to use? : #

Processing:
- Row 1: #####
- Row 2: #####
- Row 3: #####

Output:
#####
#####
#####

Total Iterations: rows × columns (i.e., 3 × 5 = 15 iterations)
"""

# Taking user input for number of rows
rows = int(input("How many Rows? : "))

# Taking user input for number of columns
columns = int(input("How many Columns? : "))

# Taking user input for the symbol to print
symbol = input("What symbol do you want to use? : ")

# Outer loop - Controls the number of rows
for i in range(rows):
    
    # Inner loop - Controls the number of columns
    for j in range(columns):
        print(symbol, end="")  # Print symbol without moving to a new line
    
    print()  # Moves to the next line after printing a full row
