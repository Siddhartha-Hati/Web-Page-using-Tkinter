import tkinter as tk
from tkinter import *
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
from PIL import ImageTk,Image
from subprocess import call

def display_data():
    try:
        table_name = table_name_entry.get()
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Babula@143',
            database='employeeshell'
        )
        cursor = conn.cursor()

        
        cursor.execute(f"SELECT * FROM {table_name}")
        data = cursor.fetchall()

        # Create a new window for displaying data
        data_window = tk.Tk()
        data_window.title("PhoneBook")

        # Create a treeview widget for displaying data in a tabular format
        tree = ttk.Treeview(data_window, columns=("Id","Name", "Contact", "Email", "Address"))
        tree.heading("#1", text="Id")
        tree.heading("#2", text="Name")
        tree.heading("#3", text="Contact")
        tree.heading("#4", text="Email")
        tree.heading("#5", text="Address")
        

        for row in data:
            tree.insert("", "end", values=row[0:5])  # Exclude the 'id' column

        tree.pack()

        # Close the connection
        conn.close()

        data_window.mainloop()
    except Error as err:
        print(f"Error: {err}")
def back():
    app.destroy()
    call(['python','employee function page.py'])

app =tk.Tk()
app.title('powerpro.com/Employee Function Page/View-Phonebook')
app.geometry('600x600')

background_image = Image.open("C:\\Users\\Siddhartha\\OneDrive\\Desktop\\python OCAC project\\foggy_day_5-wallpaper-800x600.jpg") 
background_photo = ImageTk.PhotoImage(background_image)
background_label = Label(app, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

img = ImageTk.PhotoImage(Image.open("C:\\Users\\Siddhartha\\Downloads\\logo.jpg"))
label = tk.Label(app, image = img)
label.place(x=65,y=10)

table_name_label = tk.Label(app, text="Phonebook Name").place(x=250,y=250)
table_name_entry = tk.Entry(app)
table_name_entry.place(x=240,y=275)

create_table_button = tk.Button(app, text="Open", command=display_data).place(x=250,y=310)

back_button=tk.Button(app,text='Back',command=back).place(x=320,y=310)

app.mainloop()