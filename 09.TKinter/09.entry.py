# The Entry widget allows you to create a simple textbox with a single text line.

import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.title("Entry")
root.geometry("400x200")
root.resizable(False,False)

name_entry=ttk.Entry(root)
name_entry.pack(pady=5)
name_entry.focus()

# sensitive info
password_label=ttk.Label(root,text="Password")
password_label.pack(pady=5)

password_entry=ttk.Entry(root,show="*")
password_entry.pack(pady=5)


# tracing text using StringVar()
email_var=tk.StringVar()
email_label=ttk.Label(root,text="Email")
email_label.pack(pady=5)
email_entry=ttk.Entry(root,textvariable=email_var)
email_entry.focus()
email_entry.pack(pady=5)

output_label=ttk.Label(root)
output_label.pack(pady=5)

email_var.trace_add(
    "write",
    lambda *args: output_label.config(text=email_var.get().upper())
)


root.mainloop()