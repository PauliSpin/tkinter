import tkinter as tk
from PIL import ImageTk, Image


def show():
    tk.Label(root, text=var.get()).pack()


root = tk.Tk()
root.title('Hello Python World')
root.iconbitmap('Chili_Pepper_icon.ico')
root.geometry('400x400')

var = tk.IntVar()

c = tk.Checkbutton(root, text="Check this box!", variable=var)
c.pack()

tk.Button(root, text='Show Selection', command=show).pack()

root.mainloop()
