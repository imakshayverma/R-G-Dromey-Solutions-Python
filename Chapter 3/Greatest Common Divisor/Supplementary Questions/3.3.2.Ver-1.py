def findGcd(x,y):
    if x>y:
        a=x
        b=y
    else:
        b=x
        a=y
    temp1=a
    while True:
        while temp1 >= b:
            temp1= a-b
        temp2=temp1
        a=b
        b=temp2
        temp1=a
        if temp==0:
            break
    return a
print findGcd(24,4)
