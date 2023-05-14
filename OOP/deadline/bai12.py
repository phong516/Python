"""
Tạo danh sách 2 chiều gồm 5 phần tử
Mỗi phần tử có 3 giá trị: Họ tên, MSSV, điểm
In danh sách trên
Nhập MSSV hoặc tên, xuất điểm
"""
ds=[["Nguyễn Lê Phong","20146516","9"],\
    ["Lê Phong Nguyễn","20164516","8"],\
    ["Nguyễn Phong Lê","20146615","7"],\
    ["Lê Nguyễn Phong","20164615","6"],\
    ["Phong Nguyễn Lê","20164165","5"]]
for sv in ds:  # outer loop  
    for i in sv:  # inner loop  
        print(i, end = " ") # print the elements  
    print()

mssv=input("Nhập MSSV hoặc họ tên sinh viên: ")
index=-1
for sv in ds:
    for i in sv:
        if i==mssv:
            index=ds.index(sv)
            break
if index!=-1:       
    print("Sinh viên",ds[index][0],ds[index][1],"có điểm:",ds[index][2])
else: print("Không tìm thấy dữ liệu!")  
    
