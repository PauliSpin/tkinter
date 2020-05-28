import tkinter as tk
from PIL import ImageTk, Image


def h_slide():
    tk.Label(root, text=horizontal.get()).pack()


def v_slide():
    tk.Label(root, text=vertical.get()).pack()


root = tk.Tk()
root.title('Hello Python World')
root.iconbitmap('Chili_Pepper_icon.ico')
root.geometry('400x400')

vertical = tk.Scale(root, from_=0, to=200)
vertical.pack()  # Must be on a separate line

horizontal = tk.Scale(root, from_=0, to=200, orient=tk.HORIZONTAL)
horizontal.pack()  # Must be on a separate line

tk.Button(root, text='H Value', command=h_slide).pack()

tk.Button(root, text='V Value', command=v_slide).pack()

root.mainloop()
