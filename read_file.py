"""
This program attempts to open and read a file.

Concepts Covered:
-----------------
- Using `with open(...) as file:` ensures the file is closed automatically.
- Exception handling (`try-except`) prevents crashes if the file is missing.
- The `file.closed` attribute checks if the file is properly closed.

Possible Scenarios:
--------------------
1. If the file exists: It prints the file contents.
2. If the file does NOT exist: It prints 'File not found' without crashing.
"""

try:
    # Attempting to open and read the file
    with open('/home/ea/Python/Files/test.txt') as file:
        print(file.read())  # Reading and printing file content
    
    # After exiting the 'with' block, the file is automatically closed
    print("Is the file closed?", file.closed)  # Should print: True

except FileNotFoundError:
    print('File not found')

# The file is guaranteed to be closed after exiting the 'with' block, even if an error occurs.
