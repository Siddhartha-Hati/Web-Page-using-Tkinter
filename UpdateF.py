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

            update_query = """
            UPDATE employeedetails
            SET name = IF(%s <> '', %s, name),
                age = IF(%s <> '', %s, age),
                gender = IF(%s <> '', %s, gender),
                contact_number = IF(%s <> '', %s, contact_number),
                email = IF(%s <> '', %s, email)
            WHERE Name = %s
            """
            cursor.execute(update_query, (new_name, new_name, new_age, new_age, 
                                          new_gender, new_gender, new_contact_number, new_contact_number, 
                                          new_email, new_email, username))
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
    call(['python','Admin function page.py'])


app = tk.Tk()
app.title('powerpro.com/Admin Function Page/Update-User-Data')
app.geometry('600x600')

background_image = Image.open("C:\\Users\\Siddhartha\\OneDrive\\Desktop\\python OCAC project\\foggy_day_5-wallpaper-800x600.jpg") 
background_photo = ImageTk.PhotoImage(background_image)
background_label = Label(app, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

img = ImageTk.PhotoImage(Image.open("C:\\Users\\Siddhartha\\Downloads\\logo.jpg"))
label = tk.Label(app, image = img)
label.place(x=65,y=10)


username_label = tk.Label(app, text="Enter Username:").place(x=150,y=180)
username_entry = tk.Entry(app)
username_entry.place(x=285,y=180)


new_name_label = tk.Label(app, text="New Name:").place(x=150,y=230)
new_name_entry = tk.Entry(app)
new_name_entry.place(x=285,y=230)

new_age_label = tk.Label(app, text="New Age:").place(x=150,y=280)
new_age_entry = tk.Entry(app)
new_age_entry.place(x=285,y=280)

new_gender_label = tk.Label(app, text="New Gender:").place(x=150,y=330)
new_gender_entry = tk.Entry(app)
new_gender_entry.place(x=285,y=330)

new_contact_number_label = tk.Label(app, text="New Contact Number:").place(x=150,y=380)
new_contact_number_entry = tk.Entry(app)
new_contact_number_entry.place(x=285,y=380)

new_email_label = tk.Label(app, text="New Email:").place(x=150,y=430)
new_email_entry = tk.Entry(app)
new_email_entry.place(x=285,y=430)

edit_button = tk.Button(app, text="Edit User Data", command=edit_user_data).place(x=230,y=480)

back_button=tk.Button(app,text='Back',command=back).place(x=320,y=480)

app.mainloop()