import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.title("TTK Buttons")

root.geometry("400x300")
root.resizable(False,False)

label=ttk.Label(root,text="Buttons in TTK")

# exit button
exit_button=ttk.Button(root,text="Exit",command=lambda : root.quit())
label.pack()
exit_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

root.mainloop()