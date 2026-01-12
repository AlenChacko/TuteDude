import tkinter as tk

root = tk.Tk()

# changing the window title
root.title("Title")

# changing the window size and location by geometry

# root.geometry(widthxheight±x±y)
# 600 width in pixel
# 400 height in pixel
# +50 is x the horizontal position
# -50 is y the vertical position
root.geometry("600x400+50+50")

# centering window on screen
window_width = 300
window_height = 200

# getting screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")


# resizing behavior
root.resizable(False, False)

# minsize() and maxsize()
min_width = 200
min_height = 100
root.minsize(min_width, min_height)
max_width = 700
max_height = 300
root.maxsize(max_width, max_height)

message = tk.Label(root, text="Window Label")
message.pack()

root.mainloop()
