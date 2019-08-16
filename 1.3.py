
def tver1(n):
    b=0
    while n!=0:
        a=n%10
        n=int(n/10)
        if a==1:
            b=b+a
    print(b)
tver1(a)
