"""
This script checks whether a given file or directory exists using the `os` module.

Operations performed:
1. Define the file path to be checked.
2. Use `os.path.exists(path)` to verify if the path exists.
3. If the path exists:
   - Check if it is a file using `os.path.isfile(path)`.
   - Check if it is a directory using `os.path.isdir(path)`.
4. Print appropriate messages based on the path type.

Use Cases:
✔ Validating whether a file or directory exists before performing operations on it.
✔ Avoiding errors by checking path existence before accessing files.
✔ Useful in file management, logging, and automated scripts.
"""

import os  # Importing the os module to interact with the file system

# Defining the file path to be checked
path = '/home/ea/Downloads/wp10914391-rurouni-kenshin-movie-wallpapers.jpg'

# Checking if the specified path exists
if os.path.exists(path):
    print('Location exists')  # If the path exists, print confirmation

    # Checking if the path is a file
    if os.path.isfile(path):
        print('File exists')  # If it's a file, print confirmation

    # Checking if the path is a directory
    elif os.path.isdir(path):
        print('Directory exists')  # If it's a directory, print confirmation

# If the path does not exist, print an error message
else:
    print('Location not found')
