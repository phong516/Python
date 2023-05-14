"""
Xây dựng hàm Fibonacci(n), int n
Trả về danh sách các giá trị của dãy Fibonacci có n giá trị
"""
def Fibonacci(n: int):
    f1 = 0
    f2 = 1
    ds=[]
    ds.append(f1)

    for i in range(1, int(n)):
        ds.append(f2)
        fn = f1 + f2
        f1 = f2
        f2 = fn
    return ds

n=input("Nhập giá trị nguyên: ")
while n.isdigit()==False:
    n=input("Mời nhập lại: ")
print(Fibonacci(n))