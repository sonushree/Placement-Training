def fibo(n):
    a=0
    b=1
    l=[]
    while (n>0):
        l.append(a)
        a,b =b,a+b
        n -=1
    return l
    
