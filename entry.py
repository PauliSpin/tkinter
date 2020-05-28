# https://www.youtube.com/watch?v=YXPyB4XeYLA&t=1250s
# TKinter course

import tkinter as tk

root = tk.Tk()

e = tk.Entry(root, width=50, fg='white', bg='blue', borderwidth=5)
e.pack()
prompt = 'Enter Your Name: '
e.insert(0, prompt)    # Default text in the box


def myClick():
    hello = "Hello " + e.get()
    myLabel = tk.Label(root, text=hello.replace(prompt, ''))
    myLabel.pack()


# myButton = tk.Button(root, text='Click Me!', state=tk.DISABLED) button is not clickable
# myButton = tk.Button(root, text='Click Me!', padx=50, pady=50 )

# Command needs the NAME of the function only myClick, so not myClick()
myButton = tk.Button(root, text='Enter Your Name',
                     command=myClick, fg='white', bg='red')  # Or bg='#000000' for black
myButton.pack()

root.mainloop()
