"""
Nhập int a
In tất cả số nguyên tố từ 0 đến a
"""
a=input("Nhập a: ")
while a.isdigit()==False:
    a=input("Nhập sai!!! Mời nhập lại: ")
print("Các số nguyên tố trong khoảng [0;",a,"] là: ",sep="",end=" ")
for so in range(0,int(a) + 1):  
   if so > 1:  
       for i in range(2,so):  
           if (so % i) == 0:  
               break  
       else:  
           print(so,end=" ")  