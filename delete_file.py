"""
This script demonstrates different methods for deleting files and directories using the `os` and `shutil` modules.

1. `os.remove(path)`: Deletes a specific file.
2. `os.rmdir(path)`: Deletes an empty directory but **will not** delete directories containing files.
3. `shutil.rmtree(path)`: Deletes a directory and all its contents (files and subdirectories).

The script also includes exception handling to manage potential errors:
- `FileNotFoundError`: Raised when the specified file or folder does not exist.
- `PermissionError`: Raised when the script lacks the necessary permissions to delete a file or folder.
- `OSError`: Specifically catches errors when trying to delete a non-empty folder with `os.rmdir()`.

Use Cases:
- Cleaning up temporary files and folders.
- Automating file system management tasks.
- Ensuring proper error handling when deleting directories.
"""

# Import necessary modules
import os
import shutil

# Specify the folder to be deleted
path = 'folder'

try:
    # Uncomment the following line to delete a specific file
    # os.remove(path)  

    # Attempt to delete an empty folder using os.rmdir()
    # This method will NOT work if the folder contains files or subdirectories
    # os.rmdir(path)

    # Using shutil.rmtree() to delete the folder and all its contents
    shutil.rmtree(path)

# Handling potential errors during deletion
except FileNotFoundError:
    print('File not found')  # The specified folder does not exist
except PermissionError:
    print('Permission denied')  # Lack of required permissions
except OSError:
    print('You cannot delete a folder with files using the rmdir function')  # `os.rmdir()` cannot remove non-empty folders
else:
    print('File removed')  # If no exceptions occur, deletion was successful
