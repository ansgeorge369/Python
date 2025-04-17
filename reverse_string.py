def reverse_string(text):
    """Reverse a string using slicing and loop methods.

    Args:
        text (str): Input string to reverse.
    Returns:
        tuple: (reversed string via slicing, reversed string via loop)
    """
    # Method 1: Using slicing
    slice_reverse = text[::-1]

    # Method 2: Using loop
    loop_reverse = ""
    for char in text:
        loop_reverse = char + loop_reverse  # Prepend each character

    return slice_reverse, loop_reverse

# Main program
try:
    # Get user input
    user_input = input("Enter a string to reverse: ")

    # Check for empty input
    if not user_input.strip():
        print("Error: Empty string provided.")
    else:
        # Call function to reverse string
        slice_result, loop_result = reverse_string(user_input)

        # Print results
        print(f"Original string: {user_input}")
        print(f"Reversed (slicing): {slice_result}")
        print(f"Reversed (loop): {loop_result}")

except Exception as e:
    print(f"An error occurred: {e}")