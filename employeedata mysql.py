import tkinter as tk
from tkinter import *
from tkinter import messagebox
import mysql.connector
from subprocess import call
from mysql.connector import Error
from PIL import ImageTk,Image

host='localhost'
user='root'
password='Babula@143'
database='employeeshell'
def create_table():
    try:
        table_name = table_name_entry.get()
        conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Babula@143'
        )


        cursor = conn.cursor()


        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")


        cursor.execute(f"USE {database}")


        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            Id INT AUTO_INCREMENT PRIMARY KEY,
            Name VARCHAR(255) NOT NULL UNIQUE,
            Contact VARCHAR(255) NOT NULL,
            Email VARCHAR(255) NOT NULL,
            Address VARCHAR(500) NOT NULL
        );
        """
        cursor.execute(create_table_query)


        conn.commit()
        conn.close()

        messagebox.showinfo("Success", f"Phone Book {table_name} created successfully.")
        app.destroy()
        call(['python','employee function page.py'])
    
    except Error as err:
        messagebox.showerror("Error", f"Error: {err}")
def back():
    app.destroy()
    call(['python','employee function page.py'])
        

app =tk.Tk()
app.title('powerpro.com/Employee Function Page/Create Phonebook')
app.geometry('600x600')

background_image = Image.open("C:\\Users\\Siddhartha\\OneDrive\\Desktop\\python OCAC project\\foggy_day_5-wallpaper-800x600.jpg") 
background_photo = ImageTk.PhotoImage(background_image)
background_label = Label(app, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

img = ImageTk.PhotoImage(Image.open("C:\\Users\\Siddhartha\\Downloads\\logo.jpg"))
label = tk.Label(app, image = img)
label.place(x=65,y=10)

table_name_label = tk.Label(app, text="Enter Phonebook Name").place(x=245,y=200)

table_name_entry = tk.Entry(app)
table_name_entry.place(x=250,y=225)


create_table_button = tk.Button(app, text="Create PhoneBook", command=create_table).place(x=235,y=250)

back_button=tk.Button(app,text='Back',command=back).place(x=355,y=250)


app.mainloop()