import tkinter as tk
from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
from PIL import ImageTk,Image
from subprocess import call

host='localhost'
user='root'
password='Babula@143'
database='employeeshell'

# Function to delete user data by ID
def delete_user_data():
    try:
        user_name = user_name_entry.get()

        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Babula@143',
            database='employeeshell'
        )
        cursor = conn.cursor()

        # Get the user ID by username
        cursor.execute("SELECT id FROM employeedetails WHERE Name = %s", (user_name,))
        user_id = cursor.fetchone()

        if user_id:
            user_id = user_id[0]  # Get the first column (ID) from the result

            # Delete the user record
            cursor.execute("DELETE FROM employeedetails WHERE Name = %s", (user_name,))
            conn.commit()

            # Update user IDs for users with higher IDs
            cursor.execute("UPDATE employeedetails SET id = id - 1 WHERE id > %s", (user_id,))
            conn.commit()

            messagebox.showinfo("Success", f"User '{user_name}' has been deleted. IDs have been updated.")
        else:
            # If the username doesn't exist, show an error message
            messagebox.showerror("Error", f"User '{user_name}' not found.")

        # Close the connection
        conn.close()

    except Error as err:
        messagebox.showerror("Error", f"Error: {err}")
def back():
    root.destroy()
    call(['python','Admin function page.py'])

        

root= tk.Tk()
root.title('powerpro.com/Delete employee data')
root.geometry('600x600')

background_image = Image.open("C:\\Users\\Siddhartha\\OneDrive\\Desktop\\python OCAC project\\foggy_day_5-wallpaper-800x600.jpg") 
background_photo = ImageTk.PhotoImage(background_image)
background_label = Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

img = ImageTk.PhotoImage(Image.open("C:\\Users\\Siddhartha\\Downloads\\logo.jpg"))
label = tk.Label(root, image = img)
label.place(x=65,y=10)


# Label and entry for entering user ID
user_name_label = tk.Label(root, text="Enter User Name").place(x=255,y=250)
user_name_entry = tk.Entry(root)
user_name_entry.place(x=250,y=275)

# Button to delete user data
delete_button = tk.Button(root, text="Delete User Data", command=delete_user_data).place(x=220,y=300)

back_button=tk.Button(root,text='Back',command=back).place(x=350,y=300)

# Start the main loop
root.mainloop()
