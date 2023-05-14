from tkinter import *
from tkinter.font import BOLD, ITALIC
w=Tk()  
w.geometry('300x300+600+200')

#tạo title
w.title('LENGTH CONVERSION')

#tạo label feet
l1=Label(w,text='Feet: ',font=('arial',12,ITALIC))
l1.place(x=20,y=20)

#tạo label inches
l2=Label(w,text='Inches: ',font=('arial',12,ITALIC))
l2.place(x=20,y=100)

#tạo label centimeter
l3=Label(w,text='Centimeter: ',font=('arial',12,ITALIC))
l3.place(x=20,y=130)

#tạo label báo lỗi
l4=Label(w,text='',font=('arial',13))
l4.place(x=115,y=210)


#tạo entry feet
e1=Entry(w,width=15)
e1.place(x=115,y=20)
#tạo entry inches
e2=Entry(w,width=15)
e2.place(x=115,y=100)
#tạo entry centimeter
e3=Entry(w,width=15)
e3.place(x=115,y=130)
#tạo lệnh click cho b1
def click():
    e2.delete(0,END)
    e3.delete(0,END)
    if e1.get()=='':
        feet=0
    else:
        feet=float(e1.get())
    if feet<0:
        l4.configure(text='Nhập lại giá trị') 
    else:
        inch=feet*12
        cm=feet*30.48
        e2.insert(0,str(round(inch,2)))
        e3.insert(0,str(round(cm,2)))
#tạo button convert
b1=Button(w,text='CONVERT',font=('arial',12,BOLD),bg='blue',fg='white',width=9,height=1,command=click)
b1.place(x=115,y=170)
w.mainloop()