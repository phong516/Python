from tkinter import *
from PIL import Image,ImageTk

w=Tk()
w.geometry('600x400+400+200')

w.title('Alo')

#đổi đuôi ảnh
x=Image.open('C:\\Users\\Phong\\Downloads\\smokeonthewater.jpg')
x=x.resize((200,100),Image.NEAREST)
a=ImageTk.PhotoImage(x)

#tạo ảnh
l1=Label(w,image=a)
l1.grid(row=0,column=0,padx=10,pady=20,rowspan=4)

#tạo label dưới ảnh
l2=Label(w,text='Deep Purple',font=('arial',15),fg='blue')
l2.grid(row=4,column=0,padx=30)

#command cho button b2
def b2_click():
    x=e1.get()
    l2.configure(fg=x)
    e2.configure(bg=x)
    b2.configure(fg=x)

#tạo button b2
b2=Button(w,text='Color',font=('arial',15),fg='green',command=b2_click,width=10)
b2.grid(row=2,column=1,padx=30,pady=0)

#tạo entrybox nhập
e1=Entry(w,font=('arial',15),width=10,bg='white')
e1.grid(row=1,column=1,padx=30,pady=0)
 
 #tạo entrybox đổi màu
e2=Entry(w)
e2.grid(row=3,column=1,padx=30,pady=0)

#khời tạo
w.mainloop()