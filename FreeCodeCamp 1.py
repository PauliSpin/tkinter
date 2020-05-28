# https://www.youtube.com/watch?v=YXPyB4XeYLA&t=1250s
# TKinter course

import tkinter as tk

root = tk.Tk()
# Creating a Label Widget
myLabel = tk.Label(root, text='Hello World!')
# Shoving it onto the screen
myLabel.pack()  # Packs just enough to contain the text in the Label

root.mainloop()
