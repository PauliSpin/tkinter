import tkinter as tk
from PIL import ImageTk, Image


root = tk.Tk()
root.title('Hello Python World')
root.iconbitmap('Chili_Pepper_icon.ico')

# r = tk.IntVar()  # Define a tkinter variable, you can get and set these
# r.set('2')

TOPPINGS = [
    ('Pepperoni', 'Pepperoni'),
    ('Cheese', 'Cheese'),
    ('Mushroom', 'Mushroom'),
    ('Onion', 'Onion'),
]

pizza = tk.StringVar()
pizza.set('Pepperoni')

for text, topping in TOPPINGS:
    tk.Radiobutton(root, text=text, variable=pizza,
                   value=topping).pack(anchor=tk.W)


def clicked(value):
    myLabel = tk.Label(root, text=value)
    myLabel.pack()


# tk.Radiobutton(root, text="Option 1", variable=r, value=1,
#                command=lambda: clicked(r.get())).pack()
# tk.Radiobutton(root, text="Option 2", variable=r, value=2,
#                command=lambda: clicked(r.get())).pack()

# myLabel = tk.Label(root, text=pizza.get())
# myLabel.pack()


myButton = tk.Button(root, text='Click Me!',
                     command=lambda: clicked(pizza.get()))
myButton.pack()

root.mainloop()
