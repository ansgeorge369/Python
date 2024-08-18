import tkinter
from tkinter import ttk
import serial.tools.list_ports


def get_available_ports():
    return [port.device for port in serial.tools.list_ports.comports()]


def on_connect():
    selected_connection = connection_combobox_entry.get()
    print("Selected Connection:", selected_connection)


def board_entry():
    selected_board = board_combox_entry.get()
    print("Selected Board is:", selected_board)
    # Hide the main window
    window.withdraw()
    # Create a new window
    new_window = tkinter.Toplevel(window)
    new_window.title(selected_board)
    new_window.geometry("700x600")
    # Center the new window and its title
    new_window.update_idletasks()
    width = new_window.winfo_width()
    height = new_window.winfo_height()
    x = (new_window.winfo_screenwidth() // 2) - (width // 2)
    y = (new_window.winfo_screenheight() // 2) - (height // 2)
    new_window.geometry(f"{width}x{height}+{x}+{y}")

    # Center the title
    new_window.wm_attributes("-topmost", 1)
    new_window.wm_attributes("-topmost", 0)
    # Display the selected information in the new window
    info_label = tkinter.Label(new_window)
    info_label.pack()

    # Create a frame to contain labels and set the background color
    row_frame = tkinter.Frame(new_window, bg='grey')
    row_frame.pack(pady=10)

    # Place labels at the top
    label1 = tkinter.Label(new_window, text="File", bg='grey')
    label2 = tkinter.Label(new_window, text="Script File", bg='grey')
    label3 = tkinter.Label(new_window, text="Help", bg='grey')

    label1.place(x=10, y=10)
    label2.place(x=80, y=10)
    label3.place(x=180, y=10)


def multiplier_entry():
    selected_multiplier = multiplier_combox_entry.get()
    print("Selected Multiplier is:", selected_multiplier)


# Example functions for button clicks
def on_file_click():
    print("File button clicked")


def on_script_file_click():
    print("Script File button clicked")


def on_help_click():
    print("Help button clicked")


window = tkinter.Tk()
window.title("SAM-BA CDC 3.7")
window.geometry("350x150")

# Creating widgets
connection_label = tkinter.Label(window, text="Select the Connection: ")
available_ports = get_available_ports()
connection_combobox_entry = ttk.Combobox(window, values=available_ports)
board_label = tkinter.Label(window, text="Select your Board: ")
board_combox_entry = ttk.Combobox(window, values=["at91sama5d3x-xplained", " at91sama5d2-xplained", "at91sama5d2-xplained-emmc", "at91sama5d27-som1-ek-sd", "at91sama5d27-som1-ek-optee-sd", "at91sama5d2-ptc-ek", "at91sama5d2-icp", "at91sama5d27-wlsom1-ek-sd", "at91sama5d29-curiosity-sd", "at91sama5d4ek", "at91sama5d4-xplained"])
multiplier_label = tkinter.Label(window, text="JLink Timeout Multiplier")
multiplier_combox_entry = ttk.Combobox(window, values=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"])
board_button = tkinter.Button(window, text="Connect", command=board_entry)
exit_button = tkinter.Button(window, text="Exit", command=window.quit)

# Placing widgets on the screen
connection_label.grid(row=1, column=0, pady=(10, 0))
connection_combobox_entry.grid(row=1, column=1, sticky='news', pady=(10, 0))
board_label.grid(row=2, column=0)
board_combox_entry.grid(row=2, column=1, sticky='news')
multiplier_label.grid(row=3, column=0)
multiplier_combox_entry.grid(row=3, column=1, sticky='news')
board_button.grid(row=5, column=1, pady=(20, 0))
exit_button.grid(row=5, column=2, pady=(20, 0))


window.mainloop()
