import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_label.config(text="Generated Password: " + password)

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Add some padding around the widgets
window.geometry("300x200")
window.configure(bg="#f0f0f0")

# Create and pack a frame for the content
content_frame = tk.Frame(window, bg="#f0f0f0")
content_frame.pack(pady=20, padx=10, fill=tk.BOTH)

# Create and pack labels and entry widgets
length_label = tk.Label(content_frame, text="Password Length:", bg="#f0f0f0")
length_label.pack()

length_entry = tk.Entry(content_frame)
length_entry.pack()

# Create and pack the generate button with some styling
generate_button = tk.Button(content_frame, text="Generate Password", command=generate_password, bg="#0078d4", fg="white")
generate_button.pack(pady=10, padx=20, fill=tk.X)

# Create and pack the password label with some styling
password_label = tk.Label(content_frame, text="", bg="#f0f0f0", wraplength=250)
password_label.pack()

# Center the window on the screen
window.update_idletasks()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width - window.winfo_width()) // 2
y = (screen_height - window.winfo_height()) // 2
window.geometry("+{}+{}".format(x, y))

# Start the GUI event loop
window.mainloop()
