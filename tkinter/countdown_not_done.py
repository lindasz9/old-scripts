from tkinter import *
from time import *

def counting():
    #if len(hour_str) > 2:
    #    for i in hour_str:
    #        if i == 2:
    #            hours.replace(i,None)
    time_label.config(text = hour_str+":"+
                             minute_str+":"+
                             second_str)
    window.after(1000,counting)

def clear():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)

def reset():
    pass

window = Tk()
#window.geometry("700x300")
window.configure(backgroun="black")
window.title("Countdown Timer")

hour_str = StringVar()
minute_str = StringVar()
second_str = StringVar()

hour_str.set("00")
minute_str.set("00")
second_str.set("00")

frame = Frame(window,bg="black")
frame.pack(side=TOP)

label1 = Label(frame,text="hours:",
               font=("ariel",15),
               fg="white",bg="black")
label1.grid(row=0,column=0)
entry1 = Entry(frame,font=("ariel",15),
              fg="white",bg="black",width=20,
               textvariable=hour_str)
entry1.grid(row=0,column=1)
label2 = Label(frame,text="minutes:",
               font=("ariel",15),
               fg="white",bg="black")
label2.grid(row=1,column=0)
entry2 = Entry(frame,font=("ariel",15),
              fg="white",bg="black",width=20,
               textvariable=minute_str)
entry2.grid(row=1,column=1)
label3 = Label(frame,text="seconds:",
               font=("ariel",15),
               fg="white",bg="black")
label3.grid(row=2,column=0)
entry3 = Entry(frame,font=("ariel",15),
              fg="white",bg="black",width=20,
               textvariable=second_str)
entry3.grid(row=2,column=1)

time_label = Label(window,font=("ariel",150),
                   fg="#00FF00",bg="black",
                   width=50,height=20)
time_label.pack()

button1 = Button(frame,text="reset",
                 font=("ariel", 15),
                 fg="white", bg="black",
                 command=reset)
button1.grid(row=3,column=0)
button2 = Button(frame,text="clear",
                 font=("ariel", 15),
                 fg="white", bg="black",
                 command=clear)
button2.grid(row=3,column=1)



counting()

window.mainloop()