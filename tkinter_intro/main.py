from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry("720x270")
window.title("SAM-BA v2.18")


def open_popup():
    top = Toplevel(window)
    top.geometry("720x250")
    top.title("Next Window")  # Corrected the assignment here
    Label(top, text="You had clicked a new window", font='Helvetica 14 bold').place(x=150, y=80)


Label(window, text=" Next", font='Helvetica 14 bold').pack(pady=20)
ttk.Button(window, text="Open", command=open_popup).pack()

window.mainloop()
