from tkinter import *

w=Tk()
w.geometry('600x400+400+200')

x1=IntVar(value=0)
x2=IntVar(value=0)
x3=IntVar(value=0)
x4=IntVar(value=0)

def all_pick():
    if x4.get()==1:
        c1.select()
        c2.select()
        c3.select()
    else:
        c1.deselect()
        c2.deselect()
        c3.deselect()

c1=Checkbutton(w,text='Món 1: 50.000đ',onvalue=50000,variable=x1)
c1.grid(row=0,column=0,padx=20,pady=20,sticky='w')

c2=Checkbutton(w,text='Món 2: 80.000đ',onvalue=80000,variable=x2)
c2.grid(row=1,column=0,padx=20,pady=20,sticky='w')

c3=Checkbutton(w,text='Món 3: 100.000đ',onvalue=100000,variable=x3)
c3.grid(row=2,column=0,padx=20,pady=20,sticky='w')

c4=Checkbutton(w,text='All',variable=x4, command=all_pick)
c4.grid(row=3,column=0,padx=20,pady=20,sticky='w')

def b1_click():
    t=x1.get()+x2.get()+x3.get()
    l1.configure(text='Tổng tiền: '+str(t))

b1=Button(w,text='Tính tiền',width=10,bg='blue',command=b1_click)
b1.grid(row=0,column=2,padx=20,pady=20,sticky='w')

l1=Label(w,text='Tổng tiền:')
l1.grid(row=1,column=2,padx=20,pady=20,sticky='w')

w.mainloop()