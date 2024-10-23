import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import os

# Global variable to store the username
username = ""

# Function to set the username
def set_username():
    global username
    username = name_entry.get().strip()
    if not username:
        messagebox.showwarning("Warning", "Please enter your name.")
        return
    
    username_label.config(text=f"Welcome, {username}!")
    name_entry.config(state='disabled')  # Disable the entry after setting the username
    set_username_button.config(state='disabled')  # Disable the button after setting the username

# Function to save the diary entry
def save_entry():
    entry = text_box.get("1.0", "end-1c")  # Get all text from the text box
    if not entry.strip():
        messagebox.showwarning("Warning", "Diary entry is empty!")
        return
    if not username:
        messagebox.showwarning("Warning", "Please enter your name first.")
        return

    # Get current date to use as the filename
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"diary_{username}_{today}.txt"  # Include the username in the filename

    # Save the text to a file
    with open(filename, "w") as file:
        file.write(entry)

    messagebox.showinfo("Success", f"Diary entry saved as {filename}")

# Function to load a diary entry
def load_entry():
    if not username:
        messagebox.showwarning("Warning", "Please enter your name first.")
        return

    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"diary_{username}_{today}.txt"  # Include the username in the filename
    
    if os.path.exists(filename):
        with open(filename, "r") as file:
            entry = file.read()
            text_box.delete("1.0", "end")  # Clear the text box
            text_box.insert("1.0", entry)  # Load the content into the text box
        messagebox.showinfo("Success", f"Diary entry loaded from {filename}")
    else:
        messagebox.showwarning("Warning", "No diary entry found for today.")

# Function to clear the text box
def clear_text():
    text_box.delete("1.0", "end")

# Create the main window
root = tk.Tk()
root.title("Personal Diary Application")
root.geometry("500x400")
root.minsize(400, 300)  # Set a minimum window size to avoid too small screens

# Add a label and entry for the username
name_label = tk.Label(root, text="Enter your name:")
name_label.grid(row=0, column=0, padx=10, pady=5, sticky='w')

name_entry = tk.Entry(root, font=("Arial", 12))
name_entry.grid(row=0, column=1, padx=10, pady=5)

set_username_button = tk.Button(root, text="Set Username", command=set_username, font=("Arial", 10), bg="#ADD8E6")
set_username_button.grid(row=0, column=2, padx=10, pady=5)

# Username display label
username_label = tk.Label(root, text="", font=("Arial", 12))
username_label.grid(row=1, column=0, columnspan=3, padx=10, pady=5)

# Add a text box for writing the diary entry
text_box = tk.Text(root, wrap="word", font=("Arial", 12), height=15)
text_box.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

# Create a frame to hold the buttons
button_frame = tk.Frame(root)
button_frame.grid(row=3, column=0, columnspan=3, pady=5, sticky="ew")

# Add buttons to save, load, and clear the diary entry
save_button = tk.Button(button_frame, text="Save Entry", command=save_entry, font=("Arial", 10), bg="#90EE90")
save_button.grid(row=0, column=0, padx=5, sticky="ew")

load_button = tk.Button(button_frame, text="Load Entry", command=load_entry, font=("Arial", 10), bg="#FFD700")
load_button.grid(row=0, column=1, padx=5, sticky="ew")

clear_button = tk.Button(button_frame, text="Clear Text", command=clear_text, font=("Arial", 10), bg="#FF6347")
clear_button.grid(row=0, column=2, padx=5, sticky="ew")

# Configure grid weights for proper resizing
root.grid_rowconfigure(2, weight=1)  # Allow text box to expand
root.grid_columnconfigure(0, weight=1)  # Allow left column to expand
root.grid_columnconfigure(1, weight=1)  # Allow middle column to expand
root.grid_columnconfigure(2, weight=1)  # Allow right column to expand
button_frame.grid_columnconfigure(0, weight=1)  # Ensure the buttons expand
button_frame.grid_columnconfigure(1, weight=1)
button_frame.grid_columnconfigure(2, weight=1)

# Start the main loop
root.mainloop()
