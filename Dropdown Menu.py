import tkinter as tk
from PIL import ImageTk, Image


def show():
    tk.Label(root, text=clicked.get()).pack()


root = tk.Tk()
root.title('Hello Python World')
root.iconbitmap('Chili_Pepper_icon.ico')
root.geometry('400x400')

# Drop Down Menus (Options Menu)

clicked = tk.StringVar()
# clicked.set("Monday")

choices = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

clicked.set(choices[0])

drop = tk.OptionMenu(root, clicked, *choices)
drop.pack()

tk.Button(root, text="Show Selection", command=show).pack()

root.mainloop()
