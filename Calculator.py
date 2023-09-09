import tkinter as tk

# Function to handle button clicks
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

# Function to clear the entry field
def clear():
    entry.delete(0, tk.END)

# Function to perform calculations
def calculate():
    current = entry.get()
    try:
        result = eval(current)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")  # Set the window size

# Create an entry field for input
entry = tk.Entry(root, width=30, font=("Arial", 24))
entry.grid(row=0, column=0, columnspan=4, padx=20, pady=20, ipadx=10, ipady=10)

# Create buttons for numbers and operators with improved styling
button_width = 7
button_height = 3
button_font = ("Arial", 18)

row_val = 1
col_val = 0

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, width=button_width, height=button_height, font=button_font,
              command=lambda b=button: button_click(b) if b != '=' else calculate()).grid(row=row_val, column=col_val, padx=10, pady=10)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Create a clear button with different styling
tk.Button(root, text='C', padx=20, pady=20, width=button_width, height=button_height, font=button_font, command=clear).grid(row=row_val, column=col_val, padx=10, pady=10)

# Configure column and row weights for responsive design
for i in range(4):
    root.columnconfigure(i, weight=1)
for i in range(1, 6):
    root.rowconfigure(i, weight=1)

root.mainloop()
