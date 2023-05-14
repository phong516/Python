from tkinter import *


W = Tk()
W.geometry('600x400+400+200')
W.title('CHƯƠNG TRÌNH GIAO DIỆN')


L1 = Label(master = W,text = 'Height: centimeters',font = ('arial',15))
L1.grid(row = 0,column = 0,padx=60,pady = 20,sticky = 'w')
L2 = Label(master = W,text = 'Weight: kilograms',font = ('arial',15))
L2.grid(row = 2,column = 0,padx=60,pady = 20,sticky = 'w')
E1 = Entry(master=W,font = ('arial',15),width = 10)
E1.grid(row = 1,column = 0,padx=60,pady = 0,sticky = 'w')
E2 = Entry(master=W,font = ('arial',15),width = 10)
E2.grid(row = 3,column = 0,padx=60,pady = 0,sticky = 'w')

def B1_click():
    x1 = float(E1.get())/100
    x2 = float(E2.get())
    bmi = round(x2/(x1*x1),1)
    L3.configure(text = 'BMI: ' + str(bmi))
    if bmi<18.5:
        L4.configure(text = 'THIẾU CÂN',fg = 'blue')
    elif bmi<24.9:
        L4.configure(text = 'BÌNH THƯỜNG',fg = 'green')
    elif bmi<30:
        L4.configure(text = 'THỪA CÂN',fg = 'orange')
    else:
        L4.configure(text = 'BÉO PHÌ',fg = 'red')
    
B1 = Button(master=W,text = 'CALCULATE',font = ('arial',15),fg = 'white',bg = 'blue',width = 12,command = B1_click)
B1.grid(row = 4,column = 0,padx=60,pady = 30,sticky = 'w')

L3 = Label(master = W,text = 'BMI: ',font = ('arial',15))
L3.grid(row = 1,column = 1,padx=30,pady = 0,sticky = 'w')
L4 = Label(master = W,text = '',font = ('arial',15))
L4.grid(row = 2,column = 1,padx=30,pady = 0,sticky = 'w')

#menu
menubar=Menu(W)
file=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File")
file.add_command(label="Stats")
file.add_command(label="Delete All")
file.add_command(label="Exit",command=exit)
W.config(menu=menubar)

W.mainloop()