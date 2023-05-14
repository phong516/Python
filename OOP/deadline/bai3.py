"""
Nhập giá trị C, L, f
In Z theo công thức Z=2pi*f*L-1/(2pi*f*C)
"""
from sys import getdefaultencoding
from math import pi
from math import *
c=input("Nhập giá trị điện dung C: ") 
while c.isdigit()==False: 
    c=input("Nhập sai C!!! Mời nhập lại: ")

l=input("Nhập giá trị điện cảm L: ")
while l.isdigit()==False: 
     c=input("Nhập sai L!!! Mời nhập lại: ")
    
f=input("Nhập giá trị tần số f: ")
while c.isdigit()==False: 
    c=input("Nhập sai f!!! Mời nhập lại: ")

z=abs(2*pi*int(f)*int(l)-1/(2*pi*int(f)*int(c)))
print("Tổng trở Z:",round(z),"(\u03A9)")