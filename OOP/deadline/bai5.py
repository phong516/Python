"""
Nhập số km đã đi
Tính tiền cước taxi
•	2  km đầu tiên  : 20.000 đ.
•	8  km tiếp theo : 7.000đ/km.
•	10 km tiếp theo : 5.000đ/km.
•	Từ km thứ 21 	  : 3.000đ/km

"""
km=input("Nhập số km đã đi: ")
while km.isdigit()==False:
    km=input("Nhập sai!!! Mời nhập lại: ")
km=int(km)
tien=0
if km<=2:
    tien=20000
elif km<=10:
    tien=20000+(km-2)*7000
elif km<=20:
    tien=20000+7000*8+(km-10)*5000
elif km>=21:
    tien=20000+7000*8+5000*10+(km-20)*3000
print("Tổng cước taxi:",tien,"vnđ")