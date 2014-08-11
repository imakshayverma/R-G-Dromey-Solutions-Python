def lucasSequence(n):
    a=1
    b=3
    print a
    print b
    for i in range(n-1):
        c=a+b
        a=b
        b=c
        print (c)
lucasSequence(10)
