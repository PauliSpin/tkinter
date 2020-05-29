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


# Create Update function

def update():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    record_oid = delete_box.get()

    c.execute("""
              UPDATE addresses SET 
              first_name = :first,
              last_name = :last,
              address = :address,
              city = :city,
              state = :state,
              zipcode = :zipcode
              
              WHERE oid = :oid""",
              {
                  'first': f_name_editor.get(),
                  'last': l_name_editor.get(),
                  'address': address_editor.get(),
                  'city': city_editor.get(),
                  'state': state_editor.get(),
                  'zipcode': zipcode_editor.get(),
                  'oid': record_oid
              }

              )

    conn.commit()
    conn.close()

    editor.destroy()

# Create an Edit Function


def edit():

    global editor

    editor = tk.Tk()
    editor.title('Edit a Record')
    editor.iconbitmap('Chili_Pepper_icon.ico')
    editor.geometry('400x190')

    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    record_id = delete_box.get()
    c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = c.fetchall()

    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    # Create text boxes
    f_name_editor = tk.Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))

    l_name_editor = tk.Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)

    address_editor = tk.Entry(editor, width=30)
    address_editor.grid(row=2, column=1)

    city_editor = tk.Entry(editor, width=30)
    city_editor.grid(row=3, column=1)

    state_editor = tk.Entry(editor, width=30)
    state_editor.grid(row=4, column=1)

    zipcode_editor = tk.Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1)

    # Create text box labels
    f_name_label = tk.Label(editor, text='First Name')
    f_name_label.grid(row=0, column=0, pady=(10, 0))

    l_name_label = tk.Label(editor, text='Last Name')
    l_name_label.grid(row=1, column=0)

    address_label = tk.Label(editor, text='Address')
    address_label.grid(row=2, column=0)

    city_label = tk.Label(editor, text='City')
    city_label.grid(row=3, column=0)

    state_label = tk.Label(editor, text='State')
    state_label.grid(row=4, column=0)

    zipcode_label = tk.Label(editor, text='Zipcode')
    zipcode_label.grid(row=5, column=0)

    # Loop through results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

    # Create an Save Button To Save Edited Record
    edit_btn = tk.Button(editor, text="Save Record", command=update)
    edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

    conn.commit()
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
    query_label.grid(row=12, column=0, columnspan=2)

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

delete_box_label = tk.Label(root, text='Select ID')
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

# Create an Update Button
edit_btn = tk.Button(root, text="Edit Record", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

root.mainloop()
