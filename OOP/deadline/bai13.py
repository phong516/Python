"""
Tạo danh sách 3 hàng, 2 cột. Nhập dữ liệu từ bàn phím. In danh sách
Nhập giá trị cần tìm. In vị trí (hàng, cột) của giá trị đó. Nếu không có thì nhập lại.
"""
ds=[]
for i in range(0,3):
    dscon=[]
    for j in range(0,2):
        x=input("Nhập giá trị: ")
        dscon.append(x)
    ds.append(dscon)
print("Danh sách đã nhập:")
for i in range(0,3):
    for j in range(0,2):
        print(ds[i][j],end=" ")
    print()



def timkiem():
    hang=None
    cot=None
    dem=int(0)
    find=input("Nhập giá trị cần tìm: ")
    for i in range(0,3):
        for j in range(0,2):
            if ds[i][j]==find:
                hang=i
                cot=j
                break
    if hang==None and cot==None:
        timkiem()
    else: print("Giá trị cần tìm nằm ở hàng",hang,",cột",cot)

timkiem()   