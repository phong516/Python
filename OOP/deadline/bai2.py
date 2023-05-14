"""
Nhập ngày/tháng/năm sinh(d:m:yyyy)
In riêng ngày, tháng, năm
"""
sinh=input("Nhập ngày sinh (d:m:yyyy): ")

while sinh.replace(":","1").isdigit()==False or (":" not in sinh):
    sinh=input("Nhập sai!!! Mời nhập lại:")

ngay,thang,nam=sinh.split(":")

while int(ngay)>31 or int(thang)>12:
    sinh=input("Nhập sai!!! Mời nhập lại:")
    if sinh.replace(":","1").isdigit()==True or (":" in sinh):
        ngay,thang,nam=sinh.split(":")

print("Ngày sinh: ",ngay)
print("Tháng sinh: ",thang)
print("Năm sinh: ",nam)