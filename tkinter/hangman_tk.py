from tkinter import *

def play():
    entry_word.place_forget()
    button_word.place_forget()
    word = entry_word.get()
    num = len(word)
    for i in range(num):
        #if i < (num/2):
            #place =
        label_blank = Label(window,text="_",font=("Calibri",50))
        label_blank.place()

window = Tk()
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry("%dx%d" % (width,height))
window.resizable(False,False)
window.config(background="#c79062")
window.title("Akasztófa")

entry_word = Entry(window,font=("Calibri",30),justify="center")
entry_word.place(relx=.5,rely=.4,anchor="center")

button_word = Button(window,text="PLAY",font=("Calibri",30),
                     command=play)
button_word.place(relx=.5,rely=.55,anchor="center")



window.mainloop()