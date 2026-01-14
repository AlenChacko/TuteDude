import tkinter as tk

# importing ttk module from tkinter
from tkinter import ttk

root = tk.Tk()
root.title("TTK")
tk.Label(root, text="Classic widgets").pack()
ttk.Label(root, text="Themed widgets").pack()

# 3 ways to set options for a Tk themed widget

# 1. Using the widget constructor
ttk.Label(root,text="Widget constructor").pack()

# 2. Using a dictionary index after widget creation
label=ttk.Label(root)
label['text']="Using the dictionary index"
label.pack()

# 3. Using the config() method with keyword arguments
label=ttk.Label(root)
label.config(text="Using the config method")
label.pack()


root.mainloop()



