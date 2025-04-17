def count_vowels(text):
    """Count total vowels and their frequencies in a string.

    Args:
        text (str): Input string to analyze.
    Returns:
        tuple: (total vowel count, dictionary of vowel frequencies)
    """
    # Initialize vowels and dictionary
    vowels = "aeiou"
    vowel_counts = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    total_vowels = 0

    # Convert text to lowercase for case-insensitive counting
    text = text.lower()

    # Iterate through each character
    for char in text:
        if char in vowels:
            vowel_counts[char] += 1
            total_vowels += 1

    return total_vowels, vowel_counts

# Main program
try:
    # Get user input
    user_input = input("Enter a string: ")

    # Check for empty input
    if not user_input.strip():
        print("Error: Empty string provided.")
    else:
        # Call function to count vowels
        total, frequencies = count_vowels(user_input)

        # Print results
        print(f"Total number of vowels: {total}")
        print("Vowel frequencies:")
        for vowel, count in frequencies.items():
            if count > 0:  # Only print vowels that appear
                print(f"{vowel}: {count}")
        if total == 0:
            print("No vowels found.")

except Exception as e:
    print(f"An error occurred: {e}")