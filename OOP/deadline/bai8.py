"""
Nhập họ và tên
In chữ cái đầu viết hoa, tên IN HOA
"""
hoten=input("Nhập họ và tên: ")
while hoten.replace(" ","a").isalpha==False or len(hoten)==0:
    hoten=input("Nhập sai!!! Mời nhập lại: ")

hovaten=hoten.split()
ho=hovaten[0].capitalize()
dem="false"

if len(hovaten)==2:
    ten=hovaten[1].upper()
elif len(hovaten)>=3:
    ten=hovaten[-1].upper()
    dem=hovaten[1:-1]
    dem=" ".join(dem)
    dem=dem.title()
    
if dem=="false":
    print(ho,ten,sep=" ")
else: print(ho,dem,ten,sep=" ")
