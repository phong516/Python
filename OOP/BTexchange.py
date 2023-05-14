from tkinter import *

from checkboxx import b1_click

w=Tk()
w.geometry('600x400+400+200')

w.title('MONEY EXCHANGE')

currency=IntVar(value=0)

defaultstr=StringVar(value=0)

def b1_click():
    if currency.get()==0:
        l1.configure(text='Mời chọn loại ngoại tệ')
    else:
        tien=int(e1.get())*currency.get()
        l1.configure(text='GIÁ TRỊ QUY ĐỔI: '+str(tien)+'vnđ')
        print(tien)

r1=Radiobutton(w,text='USD: 22.000',font=('arial',12),value=22000,variable=currency)
r1.grid(row=0,column=0,pady=50,padx=50,sticky='w')

r2=Radiobutton(w,text='EUR: 26.000',font=('arial',12),value=26000,variable=currency)
r2.grid(row=1,column=0,pady=0,padx=50,sticky='w')


r3=Radiobutton(w,text='JYP: 200',font=('arial',12),value=200,variable=currency)
r3.grid(row=2,column=0,pady=50,padx=50,sticky='w')

e1=Entry(w,width=20,textvariable=defaultstr)
e1.grid(row=0,column=1,sticky='w')

b1=Button(w,text='EXCHANGE',font=('timesnewroman',13),command=b1_click)
b1.grid(row=1,column=1,sticky='w')

l1=Label(w,text='GIÁ TRỊ QUY ĐỔI:    vnđ',font=('timesnewroman',14),fg='blue')
l1.grid(row=3,column=1,sticky='w')


w.mainloop()