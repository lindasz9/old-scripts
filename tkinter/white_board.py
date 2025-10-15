from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk

def display_pallete():
    id = colors.create_rectangle((10,10,30,30),fill='black')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('black'))

    id = colors.create_rectangle((10, 40, 30, 60), fill='gray')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('gray'))

    id = colors.create_rectangle((10, 70, 30, 90), fill='brown4')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('brown4'))

    id = colors.create_rectangle((10, 100, 30, 120), fill='red')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('red'))

    id = colors.create_rectangle((10, 130, 30, 150), fill='orange')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('orange'))

    id = colors.create_rectangle((10, 160, 30, 180), fill='yellow')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('yellow'))

    id = colors.create_rectangle((10, 190, 30, 210), fill='green')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('green'))

    id = colors.create_rectangle((10, 220, 30, 240), fill='blue')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('blue'))

    id = colors.create_rectangle((10, 250, 30, 270), fill='pink3')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('pink3'))

    id = colors.create_rectangle((10, 280, 30, 300), fill='purple')
    colors.tag_bind(id, '<Button-1>', lambda x: show_color('purple'))

def locate_xy(work):
    global current_x,current_y
    current_x = work.x
    current_y = work.y

def add_line(work):
    global current_x,current_y
    canvas.create_line((current_x,current_y,work.x,work.y),width=get_current_value(),
                       capstyle=ROUND,smooth=TRUE,fill=color)
    current_x,current_y = work.x,work.y

def show_color(new_color):
    global color
    color = new_color

def new_canvas():
    canvas.delete('all')
    display_pallete()

window = Tk()
window.title("White Board")
window.geometry("1050x570+150+50")
window.configure(bg="lightgray")
window.resizable(False,False)

current_x = 0
current_y = 0
color = 'black'

Button(window,text=" X ",bg="#f2f3f5",width=3,height=1,font=20,
       command=new_canvas).place(x=30,y=400)

colors = Canvas(window,bg="#ffffff",width=37,height=300,bd=0)
colors.place(x=30,y=60)

display_pallete()

canvas = Canvas(window,width=930,height=500,bg="white",cursor="hand2")
canvas.place(x=100,y=10)

canvas.bind('<Button-1>',locate_xy)
canvas.bind('<B1-Motion>',add_line)

def get_current_value():
    return '{: .2f}'.format(current_value.get())

def slider_changed(event):
    value_label.configure(text=get_current_value())

current_value = tk.DoubleVar()

slider = ttk.Scale(window,from_=0,to=100,orient='horizontal',
                   command=slider_changed,variable=current_value)
slider.place(x=30,y=530)

value_label = ttk.Label(window,text=get_current_value())
value_label.place(x=27,y=550)

window.mainloop()