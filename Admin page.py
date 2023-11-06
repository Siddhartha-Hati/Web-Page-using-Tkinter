import tkinter as tk
from tkinter import *
from subprocess import call
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector

def check_login():
    username = username_entry.get()
    password = password_entry.get()
    
    try:
        conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Babula@143',
        database='adminshell'
        )
        cursor = conn.cursor()
        
        select_query = "SELECT * FROM admindetails WHERE Name = %s AND passwords = %s"
        cursor.execute(select_query, (username, password))
        
        user_data = cursor.fetchone()
        
        conn.close()
        
        if user_data:
            messagebox.showinfo("Success", "Login Successful!")
            root.destroy()
            call(['python','Admin function page.py'])
        else:
            messagebox.showerror("Error", "Invalid Username or Password")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

def Newregistration():
    root.destroy()
    call(['python','admin phase login.py'])
def back():
    root.destroy()
    call(['python','Home page.py'])

root= tk.Tk()
root.title('powerpro.com/Admin page')
root.geometry('600x600')

background_image = Image.open("C:\\Users\\Siddhartha\\OneDrive\\Desktop\\python OCAC project\\foggy_day_5-wallpaper-800x600.jpg") 
background_photo = ImageTk.PhotoImage(background_image)
background_label = Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

img = ImageTk.PhotoImage(Image.open("C:\\Users\\Siddhartha\\Downloads\\logo.jpg"))
label = tk.Label(root, image = img)
label.place(x=65,y=30)

adminlogo=tk.Label(root,text='ADMIN',bg='Black',fg='White',font='Elephant',padx=15).place(x=240,y=135)
    
username=tk.Label(root,text='Username :',bg='green',fg='black').place(x=190,y=170)
username_entry=tk.Entry(root)
username_entry.place(x=285,y=170)

password=tk.Label(root,text='Password :',bg='green',fg='black').place(x=190,y=220)
password_entry=tk.Entry(root, show='*')
password_entry.place(x=285,y=220)

submit=tk.Button(root,text='Submit',command=check_login)
submit.place(x=250,y=265)

back=tk.Button(root,text='Back',command=back)
back.place(x=300,y=265)

newuser=tk.Button(root,text='For New User Click Here To Register',command=Newregistration)
newuser.place(x=190,y=300)

root.mainloop()