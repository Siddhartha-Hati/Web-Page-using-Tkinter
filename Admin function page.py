import tkinter as tk
from tkinter import *
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
from PIL import ImageTk,Image
from subprocess import call

host='localhost'
user='root'
password='Babula@143'
database='employeeshell'

# Function to fetch and display data from the database
def display_data():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Babula@143',
            database='employeeshell'
        )
        cursor = conn.cursor()

        # Fetch data from the 'users' table
        cursor.execute("SELECT * FROM employeedetails")
        data = cursor.fetchall()

        # Create a new window for displaying data
        data_window = tk.Tk()
        data_window.title("Employee Data")

        # Create a treeview widget for displaying data in a tabular format
        tree = ttk.Treeview(data_window, columns=("Id","Name", "Age", "Gender", "Contact Number", "Email"))
        tree.heading("#1", text="Id")
        tree.heading("#2", text="Name")
        tree.heading("#3", text="Age")
        tree.heading("#4", text="Gender")
        tree.heading("#5", text="Contact Number")
        tree.heading("#6", text="Email")

        for row in data:
            tree.insert("", "end", values=row[0:6])  # Exclude the 'id' column

        tree.pack()

        # Close the connection
        conn.close()

        data_window.mainloop()
    except Error as err:
        print(f"Error: {err}")
def display_admin_data():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Babula@143',
            database='adminshell'
        )
        cursor = conn.cursor()

        # Fetch data from the 'users' table
        cursor.execute("SELECT * FROM admindetails")
        data = cursor.fetchall()

        # Create a new window for displaying data
        admin_data_window = tk.Tk()
        admin_data_window.title("Admin Data")

        # Create a treeview widget for displaying data in a tabular format
        tree = ttk.Treeview(admin_data_window, columns=("Id","Name", "Age", "Gender", "Contact Number", "Email"))
        tree.heading("#1", text="Id")
        tree.heading("#2", text="Name")
        tree.heading("#3", text="Age")
        tree.heading("#4", text="Gender")
        tree.heading("#5", text="Contact Number")
        tree.heading("#6", text="Email")

        for row in data:
            tree.insert( "","end", values=row[0:6]) 

        tree.pack()

        # Close the connection
        conn.close()

        admin_data_window.mainloop()
    except Error as err:
        print(f"Error: {err}")
def delete():
    root.destroy()
    call(['python','delete user name and replace.py'])
def update_password():
    root.destroy()
    call(['python','Update employee password.py'])
def admin_password():
    root.destroy()
    call(['python','change admin password.py'])
def update():
    root.destroy()
    call(['python','UpdateF.py'])
def log_out():
    root.destroy()
    call(['python','Admin page.py'])
def Back():
    root.destroy()
    call(['python','Admin page.py'])
    
root= tk.Tk()
root.title('powerpro.com/Admin-Function Page')
root.geometry('600x600')

background_image = Image.open("C:\\Users\\Siddhartha\\OneDrive\\Desktop\\python OCAC project\\sandbar-wallpaper-800x600.jpg") 
background_photo = ImageTk.PhotoImage(background_image)
background_label = Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

img = ImageTk.PhotoImage(Image.open("C:\\Users\\Siddhartha\\Downloads\\logo.jpg"))
label = tk.Label(root, image = img)
label.place(x=65,y=10)
    
page_label=tk.Label(root,text='ADMIN',bg='Blue',fg='Yellow',font='Elephant')
page_label.place(x=250,y=115)

Employee_details=tk.Button(root,text='Employee Details',bg='yellow',fg='black',padx=10,command=display_data).place(x=240,y=150)


Admin_details=tk.Button(root,text='Admin Details',bg='yellow',fg='black',padx=10,command=display_admin_data).place(x=245,y=200)


Delete=tk.Button(root,text='Delete',bg='yellow',fg='black',padx=10,command=delete).place(x=265,y=250)


Update=tk.Button(root,text='Update Employee Data',bg='yellow',fg='black',padx=10,command=update).place(x=225,y=300)


change_password=tk.Button(root,text='Update Employee Password',bg='yellow',fg='black',command=update_password).place(x=220,y=350)


change_admin_password=tk.Button(root,text='Change Admin Password',bg='yellow',fg='black',command=admin_password).place(x=225,y=400)


logout=tk.Button(root,text='Logout',command=log_out)
logout.place(x=230,y=500)

back=tk.Button(root,text='Back',command=Back)
back.place(x=330,y=500)

root.mainloop()