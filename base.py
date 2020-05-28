import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox

root = tk.Tk()
root.title('Hello Python World')
root.iconbitmap('Chili_Pepper_icon.ico')

top = tk.Toplevel()
top.title('Second Window!')
top.iconbitmap('Chili_Pepper_icon.ico')
my_img = ImageTk.PhotoImage(Image.open('Amaryllis.png'))
tk.Label(top, image=my_img).pack()

tk.mainloop()
