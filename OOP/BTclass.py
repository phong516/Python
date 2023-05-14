from math import pi
class Hinh_tron:
    def __init__(self,x,y,r):
        self.x=x
        self.y=y
        self.r=r
    #Tinh dien tich
    def areacal(self):
        (self.area)=self.r*(pi**2)
        print("Dien tich hinh tron: ",round(self.area,2))
    #Tinh chu vi
    def squarecal(self):
        self.square=self.r*(pi)
        print("Chu vi hinh tron:",round(self.square,2))
    #Xac dinh 1 diem thuoc duong tron
    def Kiem_tra(self,x_0,y_0):
        self.x_0=x_0
        self.y_0=y_0
        if (x_0-self.x)**2+(y_0-self.y)**2==self.r**2:
            return True
        else: 
            return False
A=Hinh_tron(3,4,5)
A.areacal()
A.squarecal()
x0=input("Nhap toa do x:")
y0=input("Nhap toa do y:")
if A.Kiem_tra(self.x_0==x0,self.y_0=3=y0)==True:
    print ("Thuộc đường tròn")
else:
    print ("Không thuộc đường tròn")
