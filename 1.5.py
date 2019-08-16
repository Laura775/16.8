def mec5(n):
    b=0
    while n!=0:
        a=n%10
        n=int(n/10)
        if a>5:
            b=b+a
    print(b)

mec5(1242767)
