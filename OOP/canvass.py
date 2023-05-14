from tkinter import *

w=Tk()
w.geometry('1000x1000+300+300')
w.title('Vẽ CANVAS')

c1=Canvas(w,bg='white')
c1.place(x=0,y=0,width=800,height=800)

def b1_click():
    c1.create_line(50,50,50,350,350,350,350,50,50,50,width=1,fill='red')

def b2_click():
    c1.create_arc(50,50,350,350,start=0,extent=120,style=PIESLICE,width=3,outline='red',fill='blue')

def b3_click():
    c1.create_rectangle(50,50,400,400,outline='purple',fill='orange')
    c1.create_rectangle(100,100,350,350,outline='green',fill='yellow')
    c1.create_rectangle(150,150,300,300,outline='yellow',fill='green')

def b4_click():
    c1.create_oval(50,50,400,400,outline='purple',fill='orange')
    c1.create_oval(100,100,350,350,outline='green',fill='yellow')
    c1.create_oval(150,150,300,300,outline='yellow',fill='green')

def ve_hinh(event):
    x=event.x
    y=event.y
    c1.create_rectangle(x,y,x+300,x+300,outline='purple',fill='orange')
    c1.create_rectangle(x+50,y+50,x+250,y+250,outline='green',fill='yellow')
    c1.create_rectangle(x+100,y+100,x+200,y+200,outline='yellow',fill='green')

b1=Button(w,text='Line',font=('arial',15),width=12,bg='green',fg='white',command=b1_click)
b1.place(x=830,y=100)

b2=Button(w,text='Arc',font=('arial',15),width=12,bg='green',fg='white',command=b2_click)
b2.place(x=830,y=150)

b3=Button(w,text='Rec',font=('arial',15),width=12,bg='green',fg='white',command=b3_click)
b3.place(x=830,y=200)

b4=Button(w,text='Oval',font=('arial',15),width=12,bg='green',fg='white',command=b4_click)
b4.place(x=830,y=250)

c1.bind('<Button-1>',ve_hinh)

w.mainloop()