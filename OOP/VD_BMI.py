from tkinter import *
from tkinter import Menu
wi=Tk()
wi.geometry('600x400+400+200')



height=Label(wi,text='Height: Centimeter')
height.grid(row=0,column=0,pady=20,sticky='w')

heightbox=Entry(wi,width=10)
heightbox.grid(row=1,column=0,sticky='w')

weight=Label(wi,text='Weight: Kilograms')
weight.grid(row=2,column=0,pady=20,sticky='w')


weightbox=Entry(wi,width=10)
weightbox.grid(row=3,column=0,pady=20,sticky='w')

bmi=Label(wi,text='BMI')
bmi.grid(row=1,column=10,padx=30)

states=Label(wi,text='Tình trạng')
states.grid(row=2,column=10,padx=30)

def cal_cal():
    x=int(heightbox.get())/100
    y=int(weightbox.get())
    z=y/(x*2)
    bmi.configure(text=('BMI: ',z))
    if z<18.5:
        states.configure(text="Gầy")
    elif z>=18.5 and z<23:
        states.configure(text="Bình thường")
    elif z>=23:
        states.configure(text="Béo phì")

cal=Button(wi,text='Calculate',fg='green',command=cal_cal)
cal.grid(row=4,column=0,sticky='w')

def select_unit():
    if val.get()==1:
        height.configure(text='Height: Centimeters')
        weight.configure(text='Weight: Kilograms')
    if val.get()==2:
        height.configure(text='Height: Inches')
        weight.configure(text='Weight: Pounds')        

thanh_menu=Menu(master=wi)
wi.configure(menu=thanh_menu)
file_menu=Menu(thanh_menu)
thanh_menu.add_cascade(label='File',menu=file_menu)

unit_menu=Menu(wi,tearoff=False)
thanh_menu.add_cascade(label='Unit',menu=unit_menu)
val=0
unit_menu.add_radiobutton(label='Metric',value=1,variable=val,command=select_unit)
unit_menu.add_radiobutton(label='English',value=2,variable= val,command=select_unit)


wi.mainloop()