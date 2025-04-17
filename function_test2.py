def skip_multiples_of_three(n):
    for i in range(1, n + 1):  # Loop from 1 to n
        if i % 3 == 0:        # Check if i is a multiple of 3
            continue          # Skip multiples of 3
        print(i, end=", ")    # Print non-multiples

# Get input from user
try:
    n = int(input("Enter a positive integer: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        skip_multiples_of_three(n)
except ValueError:
    print("Invalid input. Please enter a valid integer.")