def func(n):
    a=0
    b=1
    c=1
    print a
    print b
    print c
    for i in range(n-2):
        d=a+b+c
        a=b
        b=c
        c=d
        print i, d

func(10)
