# Creating a window


# importing the tkinder module
import tkinter as tk

# creating the application window
root = tk.Tk()

# displaying label
message = tk.Label(root, text="Hello World")

# this statement will position the message on main window
message.pack()

# this will keep the window visible until you close it, this will call at the end of the program
root.mainloop()
