import tkinter as tk
from PIL import ImageTk, Image
import sqlite3      # Inbuilt simple DB


def show():
    tk.Label(root, text=clicked.get()).pack()


root = tk.Tk()
root.title('Hello Python World')
root.iconbitmap('Chili_Pepper_icon.ico')
root.geometry('400x400')

# Databases

# Create a database or connect to one
# Creates address_book.db if it does not already exist
conn = sqlite3.connect('address_book.db')

# Create cursor
c = conn.cursor()

# There are only 5 data Types in sqlite3:
#   1) text
#   2) integer
#   3) real
#   4) null
#   5) blob
'''
Only need to create the DB table just the once - so commented out
-----------------------------------------------------------------

# Create a table
c.execute("""CREATE TABLE addresses (
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer)""")

'''

# Any time you make a change to the database, you have to commit it
# Commit Changes
conn.commit()

# Close DB Connection
conn.close()

root.mainloop()
