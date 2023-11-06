import tkinter as tk
from tkinter import *
from subprocess import call
from PIL import ImageTk,Image

def Admin():
    root.destroy()
    call(['python','Admin page.py'])
def Employee():
    root.destroy()
    call(['python',"Employee page.py"])

root = tk.Tk()
root.geometry('600x500')
root.title("powepro.com")

background_image = Image.open("C:\\Users\\Siddhartha\\OneDrive\\Desktop\\python OCAC project\\sandbar-wallpaper-800x600.jpg") 
background_photo = ImageTk.PhotoImage(background_image)
background_label = Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

img = ImageTk.PhotoImage(Image.open("C:\\Users\\Siddhartha\\Downloads\\logo.jpg"))
label = tk.Label(root, image = img)
label.place(x=65,y=100)

admin_button = tk.Button(root, text="Admin", command=Admin)
admin_button.place(x=190,y=250)

employee_button = tk.Button(root, text="Employee", command=Employee)
employee_button.place(x=350,y=250)

root.mainloop()

