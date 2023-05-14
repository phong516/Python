from tkinter import *
from tkinter import messagebox


class Window_1:
    def __init__(self,master):
        self.master=master
        #họ tên
        self.l1=Label(master,text="HỌ VÀ TÊN:",fg='blue',font=('arial',9))
        self.l1.place(x=20,y=20)
        self.e1=Entry(master,width=20)
        self.e1.place(x=20,y=50)
        self.lb1=Listbox(master,width=20,height=15,selectmode=SINGLE)
        self.lb1.place(x=20,y=80)

#điểm số
        self.l2=Label(master,text="ĐIỂM SỐ:",fg='blue',font=('arial',9))
        self.l2.place(x=200,y=20)
        self.e2=Entry(master,width=20)
        self.e2.place(x=200,y=50)
        self.lb2=Listbox(master,width=20,height=15)
        self.lb2.place(x=200,y=80)
#add
        self.b1=Button(master,text="ADD",width=10,height=2,command=self.add,font=('arial',10))
        self.b1.place(x=350,y=120)
#delete
        self.b2=Button(master,text="DELETE",width=10,height=2,command=self.delete,font=('arial',10))
        self.b2.place(x=350,y=170)
#menu
        self.menubar=Menu(self.master)
        self.filemenu=Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label="Menu File", menu=self.filemenu)
        self.filemenu.add_command(label="Stats",command=self.stats)
        self.filemenu.add_command(label="Delete All",command=self.deleteall)
        self.filemenu.add_command(label="Exit",command=self.exit)
        self.master.config(menu=self.menubar)
        self.master.mainloop()

#hàm kiểm tra float
    def isfloat(n: str) -> bool:
        try:
            float(n)
            return True
        except ValueError:
            return False

    #hàm add
    def add(self):
        if self.e1.get()=='' and  self.e2.get()=='':
            pass
        elif self.isfloat( self.e2.get())==0:
             self.messagebox.showerror("Lỗi","Mời nhập lại giá trị")
        elif float( self.e2.get())>10:
            diem=10.0
        elif float( self.e2.get())<0:
            diem=0
        else: diem=float( self.e2.get())
        if  self.e1.get()!='' and  self.e2.get()!='' and  self.isfloat( self.e2.get())==1:
             self.lb1.insert(END, self.e1.get())
             self.lb2.insert(END,diem)
        self.e1.delete(0,END)
        self.e2.delete(0,END)
    #hàm delete
    def delete(self):
        self.i= self.lb1.index( self.lb1.curselection())
        self.lb1.delete( self.i)
        self.lb2.delete( self.i)
        


    #hàm stats
    def stats(self):
        self.a=self.lb2.get(0,self.lb2.size())
        maxi=max(self.a)
        mini=min(self.a)
        messagebox.showinfo("STATS","Điểm cao nhất: "+str(maxi)+"\n"+"Điểm thấp nhất: "+str(mini))
    #hàm deleteall
    def deleteall(self):
        self.e1.delete(0,END)
        self.e2.delete(0,END)
        self.lb1.delete(0,END)
        self.lb2.delete(0,END)

    #hàm exit
    def exit(self):
        self.yesno=self.messagebox.askyesno("EXIT","Bạn có muốn thoát không?")
        if self.yesno:
            self.master.destroy()

w=Tk()
w.geometry("450x350+500+300")
w.title("BẢNG ĐIỂM")