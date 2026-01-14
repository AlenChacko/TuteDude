import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.title("Command Binding")

ttk.Label(root,text="Assigning a callback function to specific events").pack()

root.geometry("600x300")

def button_clicked():
    print("Button Clicked")

ttk.Button(root,text="Click Me",command=button_clicked).pack()

def show_domain(option):
    print(f"Clicked {option}")

ttk.Button(root,text="Python",command=lambda: show_domain("Python")).pack()
ttk.Button(root,text="Java",command=lambda: show_domain("Java")).pack()


# Limitations
# command option isn't available for all widgets


root.mainloop()