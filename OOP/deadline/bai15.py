"""
Xây dựng hàm Arrange(A), A là 1 danh sách
Trả về danh sách đã sắp xếp từ lớn đến bé, chẵn trước, lẻ sau
"""
def Arrange(A: list):
    chan=[]
    le=[]
    for i in A:
        if int(i)%2==0:
            chan.append(i)
        else: le.append(i)
    t=0
    for i in range(0,len(chan)-1):
        for j in range(i+1,len(chan)):
            if chan[i]<chan[j]:
                t=chan[i]
                chan[i]=chan[j]
                chan[j]=t
    for i in range(0,len(le)-1):
        for j in range(i+1,len(le)):
            if le[i]<le[j]:
                t=le[i]
                le[i]=le[j]
                le[j]=t
    return chan+le

n=input("Nhập số phần tử: ")
while n.isdigit()==False:
    n=input("Mời nhập lại: ")
n=int(n)
ds=[]
for i in range(1,n+1):
    so=input("Nhập phần tử thứ "+str(i)+":")
    while so.isdigit()==False:
        so=input("Mời nhập lại: ")
    ds.append(int(so))
print(Arrange(ds))