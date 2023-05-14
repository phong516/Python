"""
Nhập 5 int vào 1 list 
In list
In max, min, average
"""
ds=[]
for i in range(0,5):
    so=input("Nhập giá trị "+str(i+1)+": ")
    while so.replace("-","1").isdigit()==False:
        so=input("Sai định dạng!!! Mời nhập giá trị "+str(i+1)+": ")
    ds.append(int(so))
print("Danh sách đã nhập:",end=" ")
for i in ds:
    print(i,end=" ")
print()
print("Giá trị lớn nhất:",max(ds))
print("Giá trị nhỏ nhất:",min(ds))
print("Giá trị trung bình:",sum(ds)/5)