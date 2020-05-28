import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox

root = tk.Tk()
root.title('Hello Python World')
root.iconbitmap('Chili_Pepper_icon.ico')


def open():
    # For some reason have to have this as local variables don't work.
    global my_img
    top = tk.Toplevel()
    top.title('Second Window!')
    top.iconbitmap('Chili_Pepper_icon.ico')
    my_img = ImageTk.PhotoImage(Image.open('Amaryllis.png'))
    tk.Label(top, image=my_img).pack()
    tk.Button(top, text='Close Window', command=top.destroy).pack()


tk.Button(root, text='Open second window', command=open).pack()


tk.mainloop()
