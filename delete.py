import tkinter as tk
from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
from PIL import ImageTk,Image

host='localhost'
user='root'
password='Babula@143'
database='employeeshell'

# Function to delete user data by ID
def delete_user_data():
    try:
        user_id = int(user_id_entry.get())  # Get the user ID from the entry field

        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Babula@143',
            database='employeeshell'
        )
        cursor = conn.cursor()

        # Check if the user ID exists in the database
        cursor.execute("SELECT * FROM employeedetails WHERE id = %s", (user_id,))
        user_data = cursor.fetchone()

        if user_data:
            # If the user ID exists, delete the user record
            cursor.execute("DELETE FROM employeedetails WHERE id = %s", (user_id,))
            conn.commit()
            messagebox.showinfo("Success", f"User with ID {user_id} has been deleted.")
        else:
            # If the user ID doesn't exist, show an error message
            messagebox.showerror("Error", f"User with ID {user_id} not found.")

        # Close the connection
        conn.close()

    except Error as err:
        messagebox.showerror("Error", f"Error: {err}")

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
user_id_label = tk.Label(root, text="Enter User ID:").place(x=250,y=250)
user_id_entry = tk.Entry(root)
user_id_entry.place(x=250,y=275)

# Button to delete user data
delete_button = tk.Button(root, text="Delete User Data", command=delete_user_data).place(x=250,y=300)

# Start the main loop
root.mainloop()
