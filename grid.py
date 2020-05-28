# https://www.youtube.com/watch?v=YXPyB4XeYLA&t=1250s
# TKinter course

import tkinter as tk

root = tk.Tk()
# Creating a Label Widget
myLabel1 = tk.Label(root, text='Hello World!')
myLabel2 = tk.Label(root, text='My Name Is Rashmi Chotalia')

# Place onto the screen, resizing doesn't move the labels
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)
# Positioning in the above is relative.

# The above can also be written on one line but not very readable:

# myLabel1 = tk.Label(root, text='Hello World!').grid(row=0, column=0)
# myLabel2 = tk.Label(
#     root, text='My Name Is Rashmi Chotalia').grid(row=1, column=0)

root.mainloop()
