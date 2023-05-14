a=int(input("Trang đầu: "))
b=int(input("Trang cuối: "))
d=0

for c in range(a,b+1):
    if ((c+d>b+1) or (c+d>b))==True:
        break
    print(c+d,c+d+1,sep=',',end=',')
    d+=3
   
d=2
print('\n')
for c in range (b,a-1,-1):
    if ((c-d<a-1) or (c-d<a))==True:
        break
    print(c-d,c-d-1,sep=',',end=',')
    d+=3
    

