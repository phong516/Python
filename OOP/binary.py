from tkinter import *

class cuaso1:
    def __init__(self, master):
        self.master = master
        self.l1=Label(master, text="Decimal")
        self.l1.place(x=50,y=40)
        self.l2=Label(master, text="Binary")
        self.l2.place(x=50,y=90)
        self.e1=Entry(master,width=12)
        self.e1.place(x=160,y=40)
        self.e2=Entry(master,width=12)
        self.e2.place(x=160,y=90)
        self.b1=Button(master,text="Convert",fg="white",bg="blue",command=self.b1_click)
        self.b1.place(x=160,y=150)

        self.menubar=Menu(self.master)
        self.filemenu=Menu(self.menubar,tearoff=0)
        
        self.filemenu.add_command(label="About")
        
        self.menubar.add_cascade(label="Menu File",menu=self.filemenu)
        self.master.config(menu=self.menubar)

    def b1_click(self):
        x=int(self.e1.get())
        y=format(x,"b")
        self.e2.delete(0,END)
        self.e2.insert(0,y)

    def open(self):
        self.a=Toplevel()
        cuaso2
class cuaso2:
    def __init__(self,master) -> None:
        self.master=master
        self.l1=Label(master,text="Binary Conversion")
        self.l1.place(x=30,y=30)
        self.l2=Label(master,text="Version: 1.0")
        self.l2.place(x=50,y=60)
        self.l3=Label(master,text="Date: 9/12/2021")
        self.l3.place(x=50,y=80)
        self.b1=Button(master,text="OK",command=self.b1_click)
        self.b1.place(x=160,y=150)
class cuaso3:
    pass

def main():
    w=Tk()
    w.geometry("400x300")
    w.title("Binary")
    app=cuaso1(master=w)
    w.mainloop()


if __name__=="__main__":
    main()