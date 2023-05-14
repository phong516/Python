n=int(input("Nhập N: "))
fn=0
fn_1=1
fn_2=0
i=0
while fn<=n:
    i+=1
    print(fn)
    fn=fn_1+fn_2
    if (fn==1) and (i==1):
        fn_2=0
    else: fn_2=fn_1
    fn_1=fn
    
    
        
    

    
