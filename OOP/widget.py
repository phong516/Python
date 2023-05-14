from tkinter import *
from tkinter.ttk import *
import tkinter

w=Tk()
w.title('Form')
w.geometry("800x600")

#label
l=tkinter.Label(w,text='Forum',fg='green',font=('YellowSubmarine',58))
l.grid(column=0,row=0)

#textbox
t=Entry(w,width=20)
t.grid(column=0,row=1)

#clickbutton
def b_click():
    l.configure(text="Hi "+t.get())
    return 

#button
b=Button(w,text='Write Hello',command=b_click)
b.grid(column=1,row=1)

#combobox
c=Combobox(w)
c['values']=("Ban1","Ban2","Ban3","Ban4")
c.grid(column=0,row=2)


w.mainloop()