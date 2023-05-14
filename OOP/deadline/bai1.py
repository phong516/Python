"""
Nhập int 3 chữ số
In: hàng trăm, hàng chục, hàng đơn vị
"""

so=input("Nhập số nguyên có 3 chữ số: ")

while len(so)!=3 or so.isdigit()==False:
    print("Nhập sai!!!")
    so=input("Mời nhập lại: ")

tram=so[0]
chuc=so[1]
donvi=so[2]

print("Hàng trăm: ",tram)
print("Hàng chục: ",chuc)
print("Hàng đơn vị: ",donvi)