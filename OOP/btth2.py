from tkinter import *
from tkinter import messagebox
w=Tk()
w.geometry("450x350+500+300")
w.title("BẢNG ĐIỂM")
#họ tên
l1=Label(w,text="HỌ VÀ TÊN:",fg='blue',font=('arial',9))
l1.place(x=20,y=20)
e1=Entry(w,width=20)
e1.place(x=20,y=50)
lb1=Listbox(w,width=20,height=15,selectmode=SINGLE)
lb1.place(x=20,y=80)

#điểm số
l2=Label(w,text="ĐIỂM SỐ:",fg='blue',font=('arial',9))
l2.place(x=200,y=20)
e2=Entry(w,width=20)
e2.place(x=200,y=50)
lb2=Listbox(w,width=20,height=15)
lb2.place(x=200,y=80)

#hàm kiểm tra float
def isfloat(n: str) -> bool:
     try:
         float(n)
         return True
     except ValueError:
         return False

#hàm add
def add():
    if e1.get()=='' and e2.get()=='':
        pass
    elif isfloat(e2.get())==0:
         messagebox.showerror("Lỗi","Mời nhập lại giá trị")
    elif float(e2.get())>10:
        diem=10.0
    elif float(e2.get())<0:
        diem=0
    else: diem=float(e2.get())
    if e1.get()!='' and e2.get()!='' and isfloat(e2.get())==1:
        lb1.insert(END,e1.get())
        lb2.insert(END,diem)
    e1.delete(0,END)
    e2.delete(0,END)
#hàm delete
def delete():
    i=lb1.index(lb1.curselection())
    lb1.delete(i)
    lb2.delete(i)
    
#add
b1=Button(w,text="ADD",width=10,height=2,command=add,font=('arial',10))
b1.place(x=350,y=120)
#delete
b2=Button(w,text="DELETE",width=10,height=2,command=delete,font=('arial',10))
b2.place(x=350,y=170)
w.mainloop()