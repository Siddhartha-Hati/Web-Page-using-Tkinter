import tkinter as tk
from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error

host='localhost'
user='root'
password='Babula@143'
database='employeeshell'

# Function to edit user data
def edit_user_data():
    try:
        username = username_entry.get()  

        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Babula@143',
            database='employeeshell'
        )
        cursor = conn.cursor()

        # Check if the username exists in the database
        cursor.execute("SELECT * FROM employeedetails WHERE Name = %s", (username,))
        user_data = cursor.fetchone()

        if user_data:
            # If the username exists, get the new data from entry fields
            new_name = new_name_entry.get()
            new_age = new_age_entry.get()
            new_gender = new_gender_entry.get()
            new_contact_number = new_contact_number_entry.get()
            new_email = new_email_entry.get()

            # Update the user record with new data
            update_query = """
            UPDATE employeedetails
            SET name = %s, age = %s, gender = %s, contact_number = %s, email = %s
            WHERE Name = %s
            """
            cursor.execute(update_query, (new_name, new_age, new_gender, new_contact_number, new_email, username))
            conn.commit()
            
            messagebox.showinfo("Success", f"User '{username}' data has been updated.")
        else:
            # If the username doesn't exist, show an error message
            messagebox.showerror("Error", f"User '{username}' not found.")

        # Close the connection
        conn.close()

    except Error as err:
        messagebox.showerror("Error", f"Error: {err}")

# Create the main application window
app = tk.Tk()
app.title("Edit User Data")

# Label and entry for entering username
username_label = tk.Label(app, text="Enter Username:")
username_label.pack()
username_entry = tk.Entry(app)
username_entry.pack()

# Labels and entries for entering new data
new_name_label = tk.Label(app, text="New Name:")
new_name_label.pack()
new_name_entry = tk.Entry(app)
new_name_entry.pack()

new_age_label = tk.Label(app, text="New Age:")
new_age_label.pack()
new_age_entry = tk.Entry(app)
new_age_entry.pack()

new_gender_label = tk.Label(app, text="New Gender:")
new_gender_label.pack()
new_gender_entry = tk.Entry(app)
new_gender_entry.pack()

new_contact_number_label = tk.Label(app, text="New Contact Number:")
new_contact_number_label.pack()
new_contact_number_entry = tk.Entry(app)
new_contact_number_entry.pack()

new_email_label = tk.Label(app, text="New Email:")
new_email_label.pack()
new_email_entry = tk.Entry(app)
new_email_entry.pack()

# Button to edit user data
edit_button = tk.Button(app, text="Edit User Data", command=edit_user_data)
edit_button.pack()

# Start the main loop
app.mainloop()
