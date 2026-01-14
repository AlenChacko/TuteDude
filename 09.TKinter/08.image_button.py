import tkinter as tk
from cmath import phase
from tkinter import ttk
from tkinter.messagebox import showinfo
from zipfile import compressor_names

from PIL.ImageOps import expand

root=tk.Tk()
root.title("Image Button")
root.geometry("300x200")
root.resizable(False,False)

def handle_click():
    showinfo(
        title="Information",
        message="Download button clicked"
    )


icon=tk.PhotoImage(file='./assets/download.png')
download_button=ttk.Button(root,image=icon,command=handle_click)
download_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

root.mainloop()