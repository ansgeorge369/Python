"""
File and Folder Relocation Script
---------------------------------
This script moves files and folders from a source location to a destination
using `os.replace()`. It checks whether the destination already exists before moving.

Key Features:
1. Moves a file (`test1.txt`) to a specified directory.
2. Moves a folder (`folder`) to a specified directory.
3. Uses exception handling to manage missing files or directories.
4. Checks if the destination exists before attempting to move.

Functions Used:
- `os.path.exists(path)`: Checks if a file/folder exists at the destination.
- `os.replace(source, destination)`: Moves a file/folder to a new location.
"""

import os  # Importing the OS module for file operations

# Moving a file
source_file = 'test1.txt'
destination_file = '/home/ea/Python/Files/test1.txt'

try:
    if os.path.exists(destination_file):
        print(f"❌ File '{destination_file}' already exists.")
    else:
        os.replace(source_file, destination_file)
        print(f"✅ File '{source_file}' moved to '{destination_file}'.")
except FileNotFoundError:
    print(f"⚠️ Error: File '{source_file}' not found.")

# Moving a folder
source_folder = 'folder'
destination_folder = '/home/ea/Python/Files/folder'

try:
    if os.path.exists(destination_folder):
        print(f"❌ Folder '{destination_folder}' already exists.")
    else:
        os.replace(source_folder, destination_folder)
        print(f"✅ Folder '{source_folder}' moved to '{destination_folder}'.")
except FileNotFoundError:
    print(f"⚠️ Error: Folder '{source_folder}' not found.")
