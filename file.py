import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog


def open():
    global my_img
    root.filename = filedialog.askopenfilename(initialdir='C:/Users/rchotalia/Documents/VisualStudioCode/TkInter',
                                               title='Select a File', filetypes=(('png files', '*.png'), ('jpg files', '*.jpg'), ('all files', '*.*')))
    tk.Label(root, text=root.filename).pack()
    my_img = ImageTk.PhotoImage(Image.open(root.filename))
    tk.Label(image=my_img).pack()


root = tk.Tk()
root.title('Hello Python World')
root.iconbitmap('Chili_Pepper_icon.ico')


tk.Button(root, text='Open File', command=open).pack()

root.mainloop()
