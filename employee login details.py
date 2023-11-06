import tkinter as tk
from tkinter import *
from subprocess import call
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
from PIL import ImageTk,Image

host='localhost'
user='root'
password='Babula@143'
database='employeeshell'

# Function to save user data to the database
def save_to_database():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_entry.get()
    contact_number = contact_number_entry.get()
    email = email_entry.get()
    passwords = password_entry.get()
    confirm_password = confirm_password_entry.get()

    if passwords != confirm_password:
        messagebox.showerror("Error", "Password and Confirm Password do not match.")
        return

    try:
        
        conn = mysql.connector.connect(
    	host='localhost',
    	user='root',
        password='Babula@143',
	    database='employeeshell'
        )

        cursor = conn.cursor()

        cursor.execute("SELECT MAX(id) FROM employeedetails")
        last_id = cursor.fetchone()[0]
        if last_id is None:
            last_id = 0

        new_id = last_id + 1

        insert_query = "INSERT INTO employeedetails (id, name, age, gender, contact_number, email, passwords) VALUES (%s,%s, %s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (new_id,name, age, gender, contact_number, email, passwords))

        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "User information saved successfully.")
    except Error as err:
        messagebox.showerror("Error", f"Error: {err}")
def Back():
    root.destroy()
    call(['python','Employee page.py'])
root= tk.Tk()
root.title('powerpro.com/Admin New Login Page')
root.geometry('600x600')

background_image = Image.open("C:\\Users\\Siddhartha\\OneDrive\\Desktop\\python OCAC project\\foggy_day_5-wallpaper-800x600.jpg") 
background_photo = ImageTk.PhotoImage(background_image)
background_label = Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

img = ImageTk.PhotoImage(Image.open("C:\\Users\\Siddhartha\\Downloads\\logo.jpg"))
label = tk.Label(root, image = img)
label.place(x=65,y=10)
    
page_label=tk.Label(root,text='EMPLOYEE',bg='Blue',fg='Yellow',font='Elephant')
page_label.place(x=230,y=115)

name=tk.Label(root,text='Name :',bg='yellow',fg='black',padx=10).place(x=150,y=150)
name_entry=tk.Entry(root)
name_entry.place(x=285,y=150)

age=tk.Label(root,text='Age :',bg='yellow',fg='black',padx=10).place(x=150,y=200)
age_entry=tk.Entry(root)
age_entry.place(x=285,y=200)

gender=tk.Label(root,text='Gender :',bg='yellow',fg='black',padx=10).place(x=150,y=250)
gender_entry=tk.Entry(root)
gender_entry.place(x=285,y=250)

contact_number=tk.Label(root,text='Contact Number :',bg='yellow',fg='black',padx=10).place(x=150,y=300)
contact_number_entry=tk.Entry(root)
contact_number_entry.place(x=285,y=300)

email=tk.Label(root,text='Email Id :',bg='yellow',fg='black',padx=10).place(x=150,y=350)
email_entry=tk.Entry(root)
email_entry.place(x=285,y=350)

password=tk.Label(root,text='Create Password :',bg='yellow',fg='black',padx=10).place(x=150,y=400)
password_entry=tk.Entry(root,show='*')
password_entry.place(x=285,y=400)

confirm_password=tk.Label(root,text='Confirm Password :',bg='yellow',fg='black',padx=10).place(x=150,y=450)
confirm_password_entry=tk.Entry(root,show='*')
confirm_password_entry.place(x=285,y=450)

submit=tk.Button(root,text='Submit',command=save_to_database)
submit.place(x=230,y=500)

back=tk.Button(root,text='Back',command=Back)
back.place(x=330,y=500)

root.mainloop()