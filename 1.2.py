def mectver(n):
    b=1
    whil n!=0:
        a=n%10
        n=int(n/10)
        if a>3:
            
            b=b*a
    print(b)
mectver(244555121)
