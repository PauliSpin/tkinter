import tkinter as tk
from PIL import ImageTk, Image


root = tk.Tk()
root.title('Hello Python World')
root.iconbitmap('Chili_Pepper_icon.ico')

# frame = tk.LabelFrame(root, text="This is my Frame. . .", padx=50, pady=50)
frame = tk.LabelFrame(root, padx=50, pady=50)
frame.pack(padx=10, pady=10)

b1 = tk.Button(frame, text="Don't Click Here")
b1.grid(row=0, column=0)

b2 = tk.Button(frame, text="... or Here")
b2.grid(row=1, column=1)

root.mainloop()
