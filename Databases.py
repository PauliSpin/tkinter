import tkinter as tk
from PIL import ImageTk, Image
import sqlite3      # Inbuilt simple DB


# Create Submit Function For Database
def submit():

    # Create a database or connect to one
    # Creates address_book.db if it does not already exist
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    c = conn.cursor()

    # Insert into the table
    # c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)")
    # f_name, l_name etc. in the line above are variables and can be called anything
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get()
              })

    # Any time you make a change to the database, you have to commit it
    # Commit Changes
    conn.commit()

    # Close DB Connection
    conn.close()

    # Clear the text boxes
    f_name.delete(0, tk.END)
    l_name.delete(0, tk.END)
    address.delete(0, tk.END)
    city.delete(0, tk.END)
    state.delete(0, tk.END)
    zipcode.delete(0, tk.END)

# Create query function


def query():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()

    # Query the Database
    # oid is the primary ID of the record which sqlite3 creates automatically
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    # c.fetchone()    # First record
    # c.fetchmany(50) # Multiple records
    # print(records)
    # Returns [('Rashmi', 'Chotalia', '36 Burwell Drive', 'Witney', 'Oxon', 123456, 1)]
    # This is a Python list containing a tuple

    print_records = ''
    for record in records:
        print_records += str(record) + "\n"
        # print_records += str(record[0]) + "\n" # First names only

    query_label = tk.Label(root, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2)
    # Commit Changes
    conn.commit()
    # Close DB Connection
    conn.close()


root = tk.Tk()
root.title('Hello Python World')
root.iconbitmap('Chili_Pepper_icon.ico')
root.geometry('400x400')

# Databases


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
# Create text boxes
f_name = tk.Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)

l_name = tk.Entry(root, width=30)
l_name.grid(row=1, column=1)

address = tk.Entry(root, width=30)
address.grid(row=2, column=1)

city = tk.Entry(root, width=30)
city.grid(row=3, column=1)

state = tk.Entry(root, width=30)
state.grid(row=4, column=1)

zipcode = tk.Entry(root, width=30)
zipcode.grid(row=5, column=1)

# Create text box labels
f_name_label = tk.Label(root, text='First Name')
f_name_label.grid(row=0, column=0)

l_name_label = tk.Label(root, text='Last Name')
l_name_label.grid(row=1, column=0)

address_label = tk.Label(root, text='Address')
address_label.grid(row=2, column=0)

city_label = tk.Label(root, text='City')
city_label.grid(row=3, column=0)

state_label = tk.Label(root, text='State')
state_label.grid(row=4, column=0)

zipcode_label = tk.Label(root, text='Zipcode')
zipcode_label.grid(row=5, column=0)

# Create Submit Button
submit_btn = tk.Button(root, text='Add Record to Database', command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a Query Button
query_btn = tk.Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

root.mainloop()
