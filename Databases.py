import tkinter as tk
from PIL import ImageTk, Image
import sqlite3      # Inbuilt simple DB


# Create function to Delete a record
def delete():
    # Create a database or connect to one
    # Creates address_book.db if it does not already exist
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    c = conn.cursor()

    # Delete a Record
    # c.execute("DELETE from addresses WHERE f_name='John'")
    #   This would delete EVERY record where the f_name is 'John'
    # The above line would delete
    c.execute("DELETE from addresses WHERE oid=" + delete_box.get())
    # Note that in the DB itself, oid is an integer but in the line above,
    # tkinter doesn't mind and converts it to a str before concatenating '+'

    # Any time you make a change to the database, you have to commit it
    # Commit Changes
    conn.commit()

    # Close DB Connection
    conn.close()

# Create Submit Function For Database


def submit():
    conn = sqlite3.connect('address_book.db')
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

    conn.commit()
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

    conn = sqlite3.connect('address_book.db')
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
        # print_records += str(record) + "\n"
        print_records += str(record[0]) + ' ' + str(record[1]) + ' ' + '\t' + \
            str(record[6]) + "\n"  # First names only

    query_label = tk.Label(root, text=print_records)
    query_label.grid(row=11, column=0, columnspan=2)

    conn.commit()
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
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))

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

delete_box = tk.Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)

# Create text box labels
f_name_label = tk.Label(root, text='First Name')
f_name_label.grid(row=0, column=0, pady=(10, 0))

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

delete_box_label = tk.Label(root, text='Delete ID')
delete_box_label.grid(row=9, column=0, pady=5)

# Create Submit Button
submit_btn = tk.Button(root, text='Add Record to Database', command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=108)

# Create a Query Button
query_btn = tk.Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=135)

# Create a Delete Button
delete_btn = tk.Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=135)

root.mainloop()
