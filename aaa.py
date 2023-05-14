t1=0
a=int(input("Nhập trang đầu: "))
b=int(input("Nhập trang cuối: "))
for c in range(a,b+1):
    if (c/2)%2==0:
        if c+1>b:
            print(c)
        else:
            print(c,c+1,sep=',',end=',')
        
        t1+=1
print('\n',"Số tờ: ",t1)
t2=0
for c in range(b,a-1,-1):
    if (c/2)%2==1:
        print(c+1,c,sep=',',end=',')
        t2+=1
print('\n',"Số tờ: ",t2)
