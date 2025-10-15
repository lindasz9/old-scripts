from tkinter import *
from tkinter import messagebox

def login():
    username = entry1.get()
    password = entry2.get()
    if (username == "" and password == ""):
        messagebox.showinfo("","Blank Not Allowed")
    elif (username == "Linda" and password == "kitten"):
        messagebox.showinfo("","Login success")
    else:
        messagebox.showinfo("","Incorrect username and password")

window = Tk()
window.title("Login")
window.geometry("300x200")

global entry1
global entry2

Label(window,text="Username:").place(x=20,y=20)
Label(window,text="Password:").place(x=20,y=70)

entry1 = Entry(window,bd=5)
entry1.place(x=140,y=20)
entry2 = Entry(window,bd=5)
entry2.place(x=140,y=70)

Button(window,text="Login",command=login,height=3,width=13,bd=6).place(x=100,y=120)

window.mainloop()