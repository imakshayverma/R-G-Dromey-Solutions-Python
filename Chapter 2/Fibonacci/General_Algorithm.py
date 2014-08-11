def fibonacci(n):
    a=0
    b=1
    print a
    print b
    for i in range(n-1):
        c=a+b
        a=b
        b=c
        print (c)
fibonacci(10)
