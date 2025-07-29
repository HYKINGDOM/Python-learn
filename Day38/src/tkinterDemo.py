import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("tkinter App")
root.geometry("300x200")

button = ttk.Button(root, text="Click Me")
button.pack(pady=50)

root.mainloop()