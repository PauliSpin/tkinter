import tkinter as tk
from PIL import ImageTk, Image


root = tk.Tk()
root.title('Hello Python World')
root.iconbitmap('Chili_Pepper_icon.ico')

my_img = ImageTk.PhotoImage(Image.open('Amaryllis.png'))
my_label = tk.Label(image=my_img)
my_label.pack()


button_quit = tk.Button(root, text='Exit Program', command=root.quit)
button_quit.pack()

root.mainloop()
