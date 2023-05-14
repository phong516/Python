from tkinter import *

w=Tk()
w.geometry('600x400+400+200')

w.title('MONEY EXCHANGE')

A=['USD: 22000','EUR: 26000','JPY: 200']
B=StringVar(value=A)

lis=Listbox(w,selectmode=SINGLE,width=15,height=8,listvariable=B)
lis.place(x=50,y=40)

currency=IntVar(value=0)


def click():
    if e1.get()=='':
        m=0
    else:
        m=float(e1.get())
    x=lis.curselection()
    if len(x)==0:
        l1.configure(text='Mời chọn ngoại tệ') 
    else:
        if x[0]==0:
            tien=m*22000
        elif x[0]==1:
            tien=m*26000
        elif x[0]==2:
            tien=m*200
        l1.configure(text='GIÁ TRỊ QUY ĐỔI: '+str(tien)+' vnđ')



e1=Entry(w,width=20)
e1.place(x=200,y=50)

b1=Button(w,text='EXCHANGE',font=('timesnewroman',13),command=click)
b1.place(x=200,y=100)

l1=Label(w,text='GIÁ TRỊ QUY ĐỔI:    vnđ',font=('timesnewroman',14),fg='blue')
l1.place(x=200,y=150)


w.mainloop()