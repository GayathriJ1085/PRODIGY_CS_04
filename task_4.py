import tkinter as tk
from tkinter import messagebox
import os

# Define the correct password
correct_password = "password"

def check_login():
    password = entry_password.get()
    
    if password == correct_password:
        root.destroy()
        os.system('python task.py')
    else:
        messagebox.showerror("Login Failed", "Invalid password")

# Set up the GUI
root = tk.Tk()
root.title("Login Page")
root.geometry("300x150")  # Set window size
root.resizable(False, False)  # Disable resizing

# Create and place widgets
label_password = tk.Label(root, text="Password:")
label_password.pack(pady=(20, 5))  # Add padding to top and bottom

entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

login_button = tk.Button(root, text="Login", command=check_login)
login_button.pack(pady=(10, 20))  # Add padding to top and bottom

root.mainloop()
