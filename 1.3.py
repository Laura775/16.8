a=[1, 5, 1, 8, 1, 1, 5]
def myfunc(n):
    b=0
    for i in a:
        if i==1:
            b=b+i
    print(b)
myfunc(a)