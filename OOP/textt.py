from tkinter import *
from tkinter import font
from tkinter import filedialog

w=Tk()
w.geometry('1000x800+400+20')
w.title('DOCUMENT EDITION')

t1=Text(w,font=('arial',15))
t1.place(x=0,y=0,width=800,height=800)

def b1_click():
    d1=filedialog.askopenfile(mode='r')
    f=open(file=d1.name,mode='r',encoding='utf-8')
    a=f.read()
    t1.delete('1.0',END)
    t1.insert('1.0',a)
    f.close()

def b2_click():
    d2=filedialog.asksaveasfile(mode='w')
    f=open(file=d2.name,mode='w',encoding='utf-8')
    f.write(t1.get('1.0',END))
    f.close()

def fontsize_change(x):
    t1.configure(font=('timesnewroman',x))


b1=Button(w,text='OPEN',font=('arial',15),width=12,bg='blue',fg='white',command=b1_click)
b1.place(x=830,y=100)

b2=Button(w,text='SAVE',font=('arial',15),width=12,bg='blue',fg='white',command=b2_click)
b2.place(x=830,y=150)

s1=Scale(w,orient='vertical',from_=8,to=20,length=400,font=('arial',15),command=fontsize_change)
s1.place(x=860,y=250)
s1.set(13)

w.mainloop()