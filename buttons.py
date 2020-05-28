# https://www.youtube.com/watch?v=YXPyB4XeYLA&t=1250s
# TKinter course

import tkinter as tk

root = tk.Tk()


def myClick():
    myLabel = tk.Label(root, text='Look! I Clicked a Button!')
    myLabel.pack()


# myButton = tk.Button(root, text='Click Me!', state=tk.DISABLED) button is not clickable
# myButton = tk.Button(root, text='Click Me!', padx=50, pady=50 )

# Command needs the NAME of the function only myClick, so not myClick()
myButton = tk.Button(root, text='Click Me!',
                     command=myClick, fg='white', bg='red')  # Or bg='#000000' for black
myButton.pack()

root.mainloop()
