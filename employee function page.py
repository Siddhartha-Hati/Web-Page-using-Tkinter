import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
from subprocess import call


def create_phonebook():
    root.destroy()
    call(['python','employeedata mysql.py'])
def view():
    root.destroy()
    call(['python','employee phonebook.py'])
def insert_data():
    root.destroy()
    call(['python','Insert phonebook.py'])
def delete():
    root.destroy()
    call(['python','delete phonebook by name.py'])
def update_password():
    root.destroy()
    call(['python','Update employee password(E).py'])
def update():
    root.destroy()
    call(['python','update phonebook.py'])
def log_out():
    root.destroy()
    call(['python','Home page.py'])
def Back():
    root.destroy()
    call(['python','Employee page.py'])
    
root= tk.Tk()
root.title('powerpro.com/Employee Function Page')
root.geometry('600x600')

background_image = Image.open("C:\\Users\\Siddhartha\\OneDrive\\Desktop\\python OCAC project\\sandbar-wallpaper-800x600.jpg") 
background_photo = ImageTk.PhotoImage(background_image)
background_label = Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

img = ImageTk.PhotoImage(Image.open("C:\\Users\\Siddhartha\\Downloads\\logo.jpg"))
label = tk.Label(root, image = img)
label.place(x=65,y=10)
    
page_label=tk.Label(root,text='EMPLOYEE',bg='Blue',fg='Yellow',font='Elephant')
page_label.place(x=250,y=115)

Create_phonebook=tk.Button(root,text='Create PhoneBoook',bg='yellow',fg='black',padx=10,command=create_phonebook).place(x=255,y=150)


phonebook=tk.Button(root,text='Phonebook',bg='yellow',fg='black',padx=10,command=view).place(x=275,y=200)


Insert_to_phonebook=tk.Button(root,text='Insert Data',bg='yellow',fg='black',padx=10,command=insert_data).place(x=278,y=250)


Delete=tk.Button(root,text='Delete',bg='yellow',fg='black',padx=10,command=delete).place(x=285,y=300)


Update=tk.Button(root,text='Update PhoneBook Data',bg='yellow',fg='black',padx=10,command=update).place(x=240,y=350)


change_password=tk.Button(root,text='Update Password',bg='yellow',fg='black',command=update_password).place(x=265,y=400)


logout=tk.Button(root,text='Logout',command=log_out)
logout.place(x=250,y=500)

back=tk.Button(root,text='Back',command=Back)
back.place(x=350,y=500)

root.mainloop()