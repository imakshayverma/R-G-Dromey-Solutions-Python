ef findGcd(x,y):
    if x>y:
        a=x
        b=y
    else :
        b=x
        a=y
    temp=1   
    while True:        
        temp=a%b
        a=b
        b=temp
        if temp==0:
            break

    return a

print findGcd(132,12)
        
        
