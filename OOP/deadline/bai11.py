"""
Nhập 1 int, nếu sai định dạng thì nhập lại
In dãy fibonacci có số phần tử bằng số đã nhập
In các số nguyên tố trong dãy fibonacci trên
"""
n=input("Nhập một số nguyên: ")
while n.isdigit()==False or n=="0":
    n=input("Mời nhập lại: ")

f1 = 0
f2 = 1
ds=[]
ds.append(f1)

for i in range(1, int(n)):
    ds.append(f2)
    fn = f1 + f2
    f1 = f2
    f2 = fn

print(n,"phần tử đầu tiên của dãy Fibonacci:",end=" ")
for i in ds:
    print(i,end=" ")
print()
print("Các số nguyên tố trong dãy Fibonacci trên:" if int(n)>4\
    else "Số nguyên tố trong dãy Fibonacci trên:" if int(n)==4 \
    else "Không có số nguyên tố trong dãy Fibonacci trên",end=" ")
    
for so in ds:
    if so > 1:  
        for i in range(2,so):  
           if (so % i) == 0:  
               break  
        else:  
           print(so,end=" ")  