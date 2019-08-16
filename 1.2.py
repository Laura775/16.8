a=[1, 2, 4, 5]
def myfunc(n):
    b=1
    for i in a:
        if i>3:
            b=b*i
    print(b)
myfunc(a)