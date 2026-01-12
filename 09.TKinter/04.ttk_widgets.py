import tkinter as tk

# importing ttk module from tkinter
from tkinter import ttk

root = tk.Tk()
tk.Label(root, text="Classic widgets").pack()
ttk.Label(root, text="Themed widgets").pack()


root.mainloop()
