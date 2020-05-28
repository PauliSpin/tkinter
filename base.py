import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox

root = tk.Tk()
root.title('Hello Python World')
root.iconbitmap('Chili_Pepper_icon.ico')

top = tk.Toplevel()
tk.Label(top, text="Hello World!").pack()

tk.mainloop()
