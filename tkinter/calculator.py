from tkinter import *

def press(num):
    global equal_text
    equal_text = equal_text + str(num)
    equal_label.set(equal_text)
def equals():
    global equal_text
    try:
        total = str(eval(equal_text))
        equal_label.set(total)
        equal_text = total
    except ZeroDivisionError:
        equal_label.set("error")
        equal_text = ""
    except SyntaxError:
        equal_label.set("error")
        equal_text = ""
def clear():
    global equal_text
    equal_label.set("")
    equal_text = ""

window = Tk()
window.title("Calculator")
window.geometry("500x600")

equal_text = ""
equal_label = StringVar()

label = Label(window,textvariable=equal_label,font=("consolas",20),bg="white",width=24,height=2)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame,text=1,height=4,width=9,font=35,
                 command=lambda: press(1))
button1.grid(row=0,column=0)
button2 = Button(frame,text=2,height=4,width=9,font=35,
                 command=lambda: press(2))
button2.grid(row=0,column=1)
button3 = Button(frame,text=3,height=4,width=9,font=35,
                 command=lambda: press(3))
button3.grid(row=0,column=2)
button4 = Button(frame,text=4,height=4,width=9,font=35,
                 command=lambda: press(4))
button4.grid(row=1,column=0)
button5 = Button(frame,text=5,height=4,width=9,font=35,
                 command=lambda: press(5))
button5.grid(row=1,column=1)
button6 = Button(frame,text=6,height=4,width=9,font=35,
                 command=lambda: press(6))
button6.grid(row=1,column=2)
button7 = Button(frame,text=7,height=4,width=9,font=35,
                 command=lambda: press(7))
button7.grid(row=2,column=0)
button8 = Button(frame,text=8,height=4,width=9,font=35,
                 command=lambda: press(8))
button8.grid(row=2,column=1)
button9 = Button(frame,text=9,height=4,width=9,font=35,
                 command=lambda: press(9))
button9.grid(row=2,column=2)
button0 = Button(frame,text=0,height=4,width=9,font=35,
                 command=lambda: press(0))
button0.grid(row=3,column=1)
plus = Button(frame,text="+",height=4,width=9,font=35,
                 command=lambda: press("+"))
plus.grid(row=0,column=3)
minus = Button(frame,text="-",height=4,width=9,font=35,
                 command=lambda: press("-"))
minus.grid(row=1,column=3)
multiply = Button(frame,text="*",height=4,width=9,font=35,
                 command=lambda: press("*"))
multiply.grid(row=2,column=3)
divide = Button(frame,text="/",height=4,width=9,font=35,
                 command=lambda: press("/"))
divide.grid(row=3,column=3)
equal = Button(frame,text="=",height=4,width=9,font=35,
                 command=equals)
equal.grid(row=3,column=2)
decimal = Button(frame,text=",",height=4,width=9,font=35,
                 command=lambda: press(","))
decimal.grid(row=3,column=0)
clear = Button(window,text="clear",height=4,width=19,font=35,
                 command=clear)
clear.pack()

window.mainloop()