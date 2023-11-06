import tkinter as tk
from tkinter import *
from subprocess import call
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
from PIL import ImageTk,Image


host = 'localhost'
user = 'root'
password = 'Babula@143'
database = 'employeeshell'


def update_password():
    try:
        username = username_entry.get()  
        old_password = old_password_entry.get() 
        new_password = new_password_entry.get()  
        confirm_password = confirm_password_entry.get()  

        if new_password == confirm_password:
            conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Babula@143',
            database='employeeshell'
            )
            cursor = conn.cursor()

            # Check if the username and old password match in the database
            cursor.execute("SELECT * FROM employeedetails WHERE Name = %s AND passwords = %s", (username, old_password))
            user_data = cursor.fetchone()

            if user_data:
                # If the username and old password match, update the user's password
                update_query = "UPDATE employeedetails SET passwords = %s WHERE Name = %s"
                cursor.execute(update_query, (new_password, username))
                conn.commit()

                messagebox.showinfo("Success", f"Password for user '{username}' has been updated.")
                app.destroy()
                call(['python','Admin function page.py'])
            else:
                # If the username and/or old password don't match, show an error message
                messagebox.showerror("Error", "Incorrect username or old password.")

            # Close the connection
            conn.close()
        else:
            # If new password and confirm password don't match, show an error message
            messagebox.showerror("Error", "New password and confirm password do not match.")

    except Error as err:
        messagebox.showerror("Error", f"Error: {err}")
def Back():
    app.destroy()
    call(['python','Admin function page.py'])

app= tk.Tk()
app.title('powerpro.com/Admin Function Page/Change-Employee_password')
app.geometry('600x600')

background_image = Image.open("C:\\Users\\Siddhartha\\OneDrive\\Desktop\\python OCAC project\\foggy_day_5-wallpaper-800x600.jpg") 
background_photo = ImageTk.PhotoImage(background_image)
background_label = Label(app, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


img = ImageTk.PhotoImage(Image.open("C:\\Users\\Siddhartha\\Downloads\\logo.jpg"))
label = tk.Label(app, image = img)
label.place(x=65,y=10)

username_label = tk.Label(app, text="Enter Username:").place(x=150,y=150)
username_entry = tk.Entry(app)
username_entry.place(x=285,y=150)

old_password_label = tk.Label(app, text="Enter Old Password:").place(x=150,y=200)
old_password_entry = tk.Entry(app, show="*") 
old_password_entry.place(x=285,y=200)

# Label and entry for entering new password
new_password_label = tk.Label(app, text="Enter New Password:").place(x=150,y=250)
new_password_entry = tk.Entry(app, show="*")
new_password_entry.place(x=285,y=250)

# Label and entry for confirming new password
confirm_password_label = tk.Label(app, text="Confirm New Password:").place(x=150,y=300)
confirm_password_entry = tk.Entry(app, show="*")
confirm_password_entry.place(x=285,y=300)

# Button to update user password
update_password_button = tk.Button(app, text="Update Password", command=update_password)
update_password_button.place(x=200,y=350)

back=tk.Button(app,text='Back',command=Back)
back.place(x=330,y=350)

# Start the main loop
app.mainloop()
