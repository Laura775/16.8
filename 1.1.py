a=[7, 11, 4, 5, 1, 7]
def myfunc(n):
    b=0
    for i in n:
        if i%2==1:
            b=b+i
    print(b)
myfunc(a)
