def fibonacci_check(d,e):
    a=0
    b=1
    c=0
    flag=0
    while c<=e:
        c=a+b
        if d==a and e==b:
            flag=1
            break
        a=b
        b=c
    if flag==1:
        print "The number are a part of fibonacci series"
    else:
        print "The numbers are not a part of fibonacci series"
        
fibonacci_check(8,12)
