import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox

root = tk.Tk()
root.title('Hello Python World')
root.iconbitmap('Chili_Pepper_icon.ico')

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno


def popup():
    # messagebox.showinfo('This is my PopUp!', 'Hello World')       # Returns ok
    # messagebox.showwarning('This is my PopUp!', 'Hello World')    # Returns ok
    # messagebox.showerror('This is my PopUp!', 'Hello World')      # Returns ok
    # messagebox.askquestion('This is my PopUp!', 'Hello World')    # Returns yes for Yes, no for No
    # messagebox.askokcancel('This is my PopUp!', 'Hello World')    # Returns 1 for  ok, 0 for cancel
    # messagebox.askyesno('This is my PopUp!', 'Hello World')       # Returns 1 for yes, 0 for no
    response = messagebox.askyesno('This is my PopUp!', 'Hello World')
    tk.Label(root, text=response).pack()
    if response == 1:
        tk.Label(root, text='You clicked Yes!').pack()
    else:
        tk.Label(root, text='You clicked No!').pack()


tk.Button(root, text='PopUp', command=popup).pack()

tk.mainloop()
