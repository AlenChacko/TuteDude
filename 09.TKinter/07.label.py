# Tkinter Label widget displays a text or image on a window.

import tkinter as tk
from tkinter import ttk
# image size adjust
from PIL import Image,ImageTk


root=tk.Tk()

root.geometry("600x400")
root.resizable(False,False)
root.title("Label demo")
# text labels
ttk.Label(root,text="Testing Label",font=("Helvetica", 14)).pack()

# image label

# resize image
# load image
img=Image.open('./assets/car.png')
# resize image to fit window
img = img.resize((300, 300), Image.Resampling.LANCZOS)

photo=ImageTk.PhotoImage(img)
# photo=tk.PhotoImage(file="./assets/car.png")
# print(photo.width(), photo.height())

label=ttk.Label(root,image=photo,padding=5)
label.pack()

root.mainloop()