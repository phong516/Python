"""
Nhập str tối đa 10 phần tử. In str
In len(str), số khoẳng trắng trong str
In str IN HOA
"""
chuoi=input("Nhập chuỗi tối đa 10 phần tử: ")
while len(chuoi)>10 or len(chuoi)==0:
    chuoi=input("Nhập sai!!! Mời nhập lại: ")

print("Chuỗi đã nhập là:",chuoi)
print("Chuỗi có",len(chuoi),"phần tử")

space=0
for i in chuoi:
    if i==" ":
        space+=1

if space==0:
    print("Chuỗi không có khoảng trắng")
else: print("Chuỗi có",space,"khoảng trắng")

print(chuoi.upper())
