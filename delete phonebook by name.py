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


def delete_user_data():
    try:
        phonebook_name=phonebook_name_entry.get()
        user_name = user_name_entry.get()

        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Babula@143',
            database='employeeshell'
        )
        cursor = conn.cursor()

        # Get the user ID by username
        cursor.execute(f"SELECT id FROM {phonebook_name} WHERE Name = %s", (user_name,))
        user_id = cursor.fetchone()

        if user_id:
            user_id = user_id[0]  # Get the first column (ID) from the result

            # Delete the user record
            cursor.execute(f"DELETE FROM {phonebook_name} WHERE Name = %s", (user_name,))
            conn.commit()

            # Update user IDs for users with higher IDs
            cursor.execute(f"UPDATE {phonebook_name} SET id = id - 1 WHERE id > %s", (user_id,))
            conn.commit()

            messagebox.showinfo("Success", f"User '{user_name}' has been deleted.")
        else:
            # If the username doesn't exist, show an error message
            messagebox.showerror("Error", f"User '{user_name}' not found.")

        # Close the connection
        conn.close()

    except Error as err:
        messagebox.showerror("Error", f"Error: {err}")

def back():
    root.destroy()
    call(['python','employee function page.py'])

        
root= tk.Tk()
root.title('powerpro.com/Employee Function Page/Delete-PhoneBook-Data')
root.geometry('600x600')

background_image = Image.open("C:\\Users\\Siddhartha\\OneDrive\\Desktop\\python OCAC project\\foggy_day_5-wallpaper-800x600.jpg") 
background_photo = ImageTk.PhotoImage(background_image)
background_label = Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


img = ImageTk.PhotoImage(Image.open("C:\\Users\\Siddhartha\\Downloads\\logo.jpg"))
label = tk.Label(root, image = img)
label.place(x=65,y=10)

phonebook_name=tk.Label(root,text='PhoneBook Name :',bg='yellow',fg='black',padx=10).place(x=250,y=200)
phonebook_name_entry=tk.Entry(root)
phonebook_name_entry.place(x=250,y=225)


# Label and entry for entering user ID
user_name_label = tk.Label(root, text="Enter Name:").place(x=250,y=250)
user_name_entry = tk.Entry(root)
user_name_entry.place(x=250,y=275)

# Button to delete user data
delete_button = tk.Button(root, text="Delete User Data", command=delete_user_data).place(x=230,y=300)

back_button=tk.Button(root, text='Back', command=back).place(x=350,y=300)

# Start the main loop
root.mainloop()
