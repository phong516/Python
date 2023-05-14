from tkinter import *
A=Tk()
A.geometry('800x600+400+200')
A.title('Chương trình giao diện')


def B1_click():
    A.destroy()

B1=Button(master=A,text='OK',font=('arial',15),width=12,fg='blue',command=B1_click)
B1.place(x=230,y=130,)

def B2_click():
    A.geometry('400x200+400+200')

B2=Button(master=A,text='Reside',font=('arial',15),width=12,fg='green',command=B2_click)
B2.place(x=450,y=130)

B3=Button(master=A,text='Close',font=('arial',15),width=12,fg='red',command=B2_click)
B3.place(x=230,y=200)

B4=Button(master=A,text='Cancel',font=('arial',15),width=12,fg='orange',command=B2_click)
B4.place(x=450,y=200)


A.mainloop()