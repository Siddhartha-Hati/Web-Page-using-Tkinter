import tkinter as tk
from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
from subprocess import call
from PIL import ImageTk,Image


host='localhost'
user='root'
password='Babula@143'
database='employeeshell'

# Function to edit user data
def edit_user_data():
    try:
        phonebook_name=phonebook_name_entry.get()
        username = username_entry.get()  

        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Babula@143',
            database='employeeshell'
        )
        cursor = conn.cursor()

        # Check if the username exists in the database
        cursor.execute(f"SELECT * FROM {phonebook_name} WHERE name = %s", (username,))
        user_data = cursor.fetchone()

        if user_data:
            # If the username exists, get the new data from entry fields
            new_name = new_name_entry.get()
            new_contact_number = new_contact_number_entry.get()
            new_email = new_email_entry.get()
            new_address = new_address_entry.get()

            update_query = f"""
            UPDATE {phonebook_name}
            SET name = IF(%s <> '', %s, name),
                contact = IF(%s <> '', %s, contact),
                email = IF(%s <> '', %s, email),
                address = IF(%s <> '', %s, address)
            WHERE Name = %s
            """
            cursor.execute(update_query, (new_name, new_name, new_contact_number, new_contact_number,new_email, new_email, new_address,new_address,username))
            conn.commit()
            
            messagebox.showinfo("Success", f"User '{username}' data has been updated.")
        else:
            # If the username doesn't exist, show an error message
            messagebox.showerror("Error", f"User '{username}' not found.")

        # Close the connection
        conn.close()

    except Error as err:
        messagebox.showerror("Error", f"Error: {err}")
def back():
    app.destroy()
    call(['python','employee function page.py'])

# Create the main application window
app =tk.Tk()
app.title('powerpro.com/Employee Function Page/Update-Phonebook')
app.geometry('600x600')

background_image = Image.open("C:\\Users\\Siddhartha\\OneDrive\\Desktop\\python OCAC project\\foggy_day_5-wallpaper-800x600.jpg") 
background_photo = ImageTk.PhotoImage(background_image)
background_label = Label(app, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

img = ImageTk.PhotoImage(Image.open("C:\\Users\\Siddhartha\\Downloads\\logo.jpg"))
label = tk.Label(app, image = img)
label.place(x=65,y=10)


phonebook_name_label = tk.Label(app, text="PhoneBook Name:").place(x=150,y=180)
phonebook_name_entry = tk.Entry(app)
phonebook_name_entry.place(x=285,y=180)


# Label and entry for entering username
username_label = tk.Label(app, text="Enter Name:").place(x=150,y=230)
username_entry = tk.Entry(app)
username_entry.place(x=285,y=230)

# Labels and entries for entering new data
new_name_label = tk.Label(app, text="New Name:").place(x=150,y=280)
new_name_entry = tk.Entry(app)
new_name_entry.place(x=285,y=280)


new_contact_number_label = tk.Label(app, text="New Contact Number:").place(x=150,y=330)
new_contact_number_entry = tk.Entry(app)
new_contact_number_entry.place(x=285,y=330)

new_email_label = tk.Label(app, text="New Email:").place(x=150,y=380)
new_email_entry = tk.Entry(app)
new_email_entry.place(x=285,y=380)


new_address_label = tk.Label(app, text="New Address:").place(x=150,y=430)
new_address_entry = tk.Entry(app)
new_address_entry.place(x=285,y=430)

# Button to edit user data
edit_button = tk.Button(app, text="Edit User Data", command=edit_user_data).place(x=230,y=480)

back_button=tk.Button(app,text='Back',command=back).place(x=320,y=480)
# Start the main loop
app.mainloop()