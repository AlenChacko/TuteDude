# Tkinter uses the geometry manager to arrange widgets on a window or frame.
# by default pack sets the widgets in one direction top to bottom
# Tkinter supports three geometry managers:
# pack
# grid
# place


# 1. pack
    # Side
    # Expand
    # Fill
    # ipadx, ipady
    # padx, pady
    # Anchor


import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.title("Geometry Managers")
root.geometry("600x300")
root.resizable(False,False)

# side - determines the direction of the widgets(top,bottom,left,right)
# top is the default
"""
label1 = tk.Label(root, text='Tkinter',bg='red',fg='white')
label2 = tk.Label(root,text='Pack Layout',bg='green', fg='white')
label3 = tk.Label(root, text='Demo',bg='blue', fg='white')

label1.pack(side=tk.LEFT)
label2.pack(side=tk.LEFT)
label3.pack(side=tk.LEFT)
"""

# expand - determines whether the widget should expand to occupy any extra spaces allocated to the container.
# If set to True, widget will expand, if False take only necessary space
"""
label4 = tk.Label(root, text='Tkinter',bg='green',fg='white')
label5 = tk.Label(root,text='Pack Layout',bg='orange', fg='white')
label6 = tk.Label(root, text='Demo',bg='yellow', fg='white')

label4.pack(side=tk.TOP,expand=True)
label5.pack(side=tk.TOP,expand=True)
label6.pack(side=tk.TOP,expand=True)
"""

# fill - determines if a widget will occupy the available space,
# accepts the x,y,both and NONE values, by default is NONE
# NONE - no extra space
# x - x axis,  expand horizontally to fill any extra space along the x-axis.
# y - y axis, expand vertically to fill any extra space along the y-axis.
# both - expand both horizontally and vertically to fill any extra space in both directions.
"""label1 = tk.Label(root, text='Tkinter',bg='red',fg='white')
label2 = tk.Label(root,text='Pack Layout',bg='green', fg='white')
label3 = tk.Label(root, text='Fill',bg='blue', fg='white')
label4 = tk.Label(root, text='Demo',bg='purple', fg='white')

label1.pack(side=tk.TOP, expand=True, fill=tk.X)
label2.pack(side=tk.TOP, expand=True, fill=tk.Y)
label3.pack(side=tk.TOP, expand=True, fill=tk.NONE)
label4.pack(side=tk.TOP, expand=True, fill=tk.BOTH)"""

# ipadx, ipady - creates internal paddings for widgets
# ipadx creates padding left and right, or padding along the x-axis.
# ipady creates padding top and bottom, or padding along the y-axis.
"""label1 = tk.Label(root, text='Pack',bg='red',fg='white')
label2 = tk.Label(root,text='Pack',bg='green', fg='white')
label3 = tk.Label(root, text='Pack',bg='blue', fg='white')
label4 = tk.Label(root, text='Pack',bg='purple', fg='white')

label1.pack(side=tk.LEFT)
label2.pack(side=tk.LEFT, ipadx=40)
label3.pack(side=tk.LEFT, ipady=40)
label4.pack(side=tk.LEFT, ipadx=80, ipady=80)"""

# padx,pady - external paddings for widgets
# padx – represents the horizontal padding that adds space to the left and right of the widget.
# pady – represents the vertical padding that adds space above or below the widget.

"""label1 = tk.Label(root, text='Pack',bg='red',fg='white')
label2 = tk.Label(root, text='Pack',bg='green', fg='white')
label3 = tk.Label(root, text='Pack',bg='blue', fg='white')
label4 = tk.Label(root, text='Pack',bg='purple', fg='white')

label1.pack(side=tk.TOP, fill=tk.X, pady=10)
label2.pack(side=tk.TOP, fill=tk.X, pady=20)
label3.pack(side=tk.TOP, fill=tk.X ,pady=40)
label4.pack(side=tk.TOP, fill=tk.X, pady=60)"""

# The anchor parameter allows you to anchor the widget to the edge of the allocated space.
# It accepts one of the following values:
# Sticky	Description
# ‘n’	North or Top Center
# ‘s’	South or Bottom Center
# ‘e’	East or Right Center
# ‘w’	West or Left Center
# ‘nw’	North West or Top Left
# ‘ne’	North East or Top Right
# ‘se’	South East or Bottom Right
# ‘sw’	South West or Bottom Left
# ‘center’	Center

"""box1 = tk.Label(root, text="Box 1", bg="green", fg="white")
box1.pack(ipadx=20, ipady=20, anchor=tk.E,  expand=True)

# box 2
box2 = tk.Label(root, text="Box 2", bg="red", fg="white")
box2.pack(ipadx=20, ipady=20, anchor=tk.W, expand=True)"""

root.mainloop()