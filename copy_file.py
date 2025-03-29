"""
This script demonstrates three different file copying methods from the `shutil` module:

1. `shutil.copyfile(src, dst)`: Copies the contents of `src` to `dst`. 
   - Only works with file paths (not directories).
   - Does NOT copy metadata like permissions or timestamps.

2. `shutil.copy(src, dst)`: Copies the file and **preserves permissions** but not other metadata.

3. `shutil.copy2(src, dst)`: Copies the file and **preserves metadata** (timestamps, permissions, etc.).

Use Cases:
- Creating backups of files.
- Duplicating files while preserving metadata when needed.
- Moving files between directories while keeping file attributes intact.
"""

# Importing the shutil module for file operations
import shutil

# Using shutil.copyfile() to copy the contents of 'test.txt' into 'copy.txt'
shutil.copyfile('test.txt', 'copy.txt')  

# Note: `shutil.copyfile()` only copies the file content, 
# but does not preserve metadata like creation/modification timestamps.

# If copying to another directory, provide the full destination path.
# Example: shutil.copyfile('test.txt', '/path/to/destination/copy.txt')
