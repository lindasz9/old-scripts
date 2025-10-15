from tkinter import *
from datetime import date

def calculate():
    today = date.today()
    birth_date = date(int(year_entry.get()),int(month_entry.get()),int(day_entry.get()))
    age = today.year-birth_date.year-((today.month,today.day)<(birth_date.month,birth_date.day))
    Label(text=f"{name_value.get()}, your age is {age}.",font=30).place(x=200,y=450)

window = Tk()

window.geometry("600x600")
window.resizable(False,False)
window.title("Age Calculator")

Label(text="Name:",font=25).place(x=100,y=150)
Label(text="Year:",font=25).place(x=100,y=200)
Label(text="Month:",font=25).place(x=100,y=250)
Label(text="Day:",font=25).place(x=100,y=300)

name_value = StringVar()
year_value = StringVar()
month_value = StringVar()
day_value = StringVar()

name_entry = Entry(window,textvariable=name_value,width=30,bd=3,font=20)
name_entry.place(x=200,y=150)
year_entry = Entry(window,textvariable=year_value,width=30,bd=3,font=20)
year_entry.place(x=200,y=200)
month_entry = Entry(window,textvariable=month_value,width=30,bd=3,font=20)
month_entry.place(x=200,y=250)
day_entry = Entry(window,textvariable=day_value,width=30,bd=3,font=20)
day_entry.place(x=200,y=300)

Button(text="Calculate",font=20,bg="black",fg="white",width=10,height=1,command=calculate).place(x=270,y=350)

window.mainloop()