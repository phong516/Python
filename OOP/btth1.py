from tkinter import *
from tkinter import messagebox
w=Tk()
w.geometry("250x200+500+300")
w.title("BINARY CONVERSION")
#decimal
l1=Label(w,text="DECIMAL:",font=('arial',9))
l1.place(x=20,y=30)
e1=Entry(w,width=15)
e1.place(x=80,y=30)

#binary
l2=Label(w,text="BINARY:",font=('arial',9))
l2.place(x=20,y=70)
e2=Entry(w,width=15)
e2.place(x=80,y=70)

#hàm đổi giá trị convert
def convert():
    e2.delete(0,END)
    if e1.get()=='':
        x=0
    elif e1.get().isdigit()==1:
        x=int(e1.get())
    else: x=-1
    if x<0:
        messagebox.showerror("Lỗi","Nhập sai định dạng giá trị")
    else:
        binary=format(x,"b")
        e2.insert(0,str(binary))

#convert
b1=Button(w,text="CONVERT",width=12,fg="white",bg="blue",command=convert,font=('arial',10))
b1.place(x=80,y=110)



w.mainloop()