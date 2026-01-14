# Assigning a function to an event of a widget is known as event binding.

import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.title("Event Binding")
root.geometry("600x400")

def return_pressed(event):
    print(f"Return Key Pressed")

def log(event):
    print(event)
btn=ttk.Button(root,text="Save")
btn.bind('<Return>',return_pressed)

# adding more
btn.bind('<Return>',log,add="+")
btn.focus()
btn.pack(expand=True)

root.mainloop()