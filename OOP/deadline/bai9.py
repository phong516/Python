"""
Nhập chuỗi tối đa 50 kí tự 
Xóa tất cả khoảng trắng, in chuỗi mới
"""
chuoi=input("Nhập chuỗi: ")
while len(chuoi)>50 or len(chuoi)==0:
    chuoi=input("Mời nhập lại: ")
chuoi=chuoi.replace(" ","")
print("Chuỗi mới:",chuoi)