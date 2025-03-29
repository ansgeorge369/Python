"""
Appending Data to a Text File:
------------------------------
- This script **opens a file in append mode ('a')** to add new content without erasing existing data.
- If the file does not exist, it will **automatically create one**.
- The added text will appear at the **end** of the file.

💡 Key Concepts Used:
- **`open('filename', 'a')`**: Opens a file in **append mode**.
- **`.write()`**: Writes new data at the end of the file.
- **File Handling with `with` Statement**: Ensures the file is properly closed.
"""

# Original text to be added
text = "Yocto is a build system for creating custom Linux distributions for embedded systems.\n"

# Open file in append mode ('a') to add content
with open("test.txt", "a") as file:
    file.write(text)  # Append the text

print("Data appended successfully!")  # Confirmation message
