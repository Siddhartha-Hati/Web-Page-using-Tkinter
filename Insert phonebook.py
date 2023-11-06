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
database='adminshell'

# Function to save user data to the database
def save_to_phonebook():
    phonebook_name=phonebook_name_entry.get()
    name = name_entry.get()
    contact = contact_number_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    
    try:
        

        conn = mysql.connector.connect(
    	host='localhost',
    	user='root',
        password='Babula@143',
	database='employeeshell'
        )

        cursor = conn.cursor()
        cursor.execute(f"SELECT MAX(id) FROM {phonebook_name}")
        last_id=cursor.fetchone()[0]
        if last_id is None:
            last_id=0

        insert_query = f"INSERT INTO {phonebook_name} (id,name,contact, email, address) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (last_id+1,name,contact, email,address))

        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "User information saved successfully.")
        
    except Error as err:
        messagebox.showerror("Error", f"Error: {err}")
def Back():
    root.destroy()
    call(['python','employee function page.py'])
root= tk.Tk()
root.title('powerpro.com/Employee function page/Insert-into-PhoneBook')
root.geometry('600x600')

background_image = Image.open("C:\\Users\\Siddhartha\\OneDrive\\Desktop\\python OCAC project\\foggy_day_5-wallpaper-800x600.jpg") 
background_photo = ImageTk.PhotoImage(background_image)
background_label = Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

img = ImageTk.PhotoImage(Image.open("C:\\Users\\Siddhartha\\Downloads\\logo.jpg"))
label = tk.Label(root, image = img)
label.place(x=65,y=10)

phonebook_name=tk.Label(root,text='PhoneBook Name :',bg='yellow',fg='black',padx=10).place(x=150,y=150)
phonebook_name_entry=tk.Entry(root)
phonebook_name_entry.place(x=285,y=150)


name=tk.Label(root,text='Name :',bg='yellow',fg='black',padx=10).place(x=150,y=200)
name_entry=tk.Entry(root)
name_entry.place(x=285,y=200)


contact_number=tk.Label(root,text='Contact Number :',bg='yellow',fg='black',padx=10).place(x=150,y=250)
contact_number_entry=tk.Entry(root)
contact_number_entry.place(x=285,y=250)

email=tk.Label(root,text='Email Id :',bg='yellow',fg='black',padx=10).place(x=150,y=300)
email_entry=tk.Entry(root)
email_entry.place(x=285,y=300)

address=tk.Label(root,text='Address :',bg='yellow',fg='black',padx=10).place(x=150,y=350)
address_entry=tk.Entry(root)
address_entry.place(x=285,y=350)

submit=tk.Button(root,text='Submit',command=save_to_phonebook)
submit.place(x=230,y=500)

back=tk.Button(root,text='Back',command=Back)
back.place(x=330,y=500)

root.mainloop()