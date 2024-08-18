import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.title("Login-Form")
window.geometry("500x350")
window.configure(bg='#444444')

def login():
    username = "Ans"
    password = "ABCD"
    if username_entry.get() == username and password_entry.get() == password:
        messagebox.showinfo(title='Login Success', message='Credentials Verified! Login Valid')
    else:
        messagebox.showinfo(title='Login Failed', message='Invalid Credentials!')

frame = tkinter.Frame(bg='#444444')
# creating widgets
login_label = tkinter.Label(frame, text="Login Page", bg='#444444', fg='#ABCDEF', font=('Ariel', 20))
username_label = tkinter.Label(frame, text="Username: ", bg='#444444', fg='#FFFFFF', font=('Ariel', 15))
username_entry = tkinter.Entry(frame, font=('Ariel', 15))
password_label = tkinter.Label(frame, text="Password: ", bg='#444444', fg='#FFFFFF', font=('Ariel', 15))
password_entry = tkinter.Entry(frame, show='*', font=('Ariel', 15))
login_button = tkinter.Button(frame, text="Login", bg='#FF5555', fg='#FFFFFF', font=('Ariel', 15), command=login)

# Placing widgets on the screen

login_label.grid(row=0, column=1, columnspan=2, sticky='news', pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=20)

frame.pack()

window.mainloop()