def findGcd(x,y):
    if x>y:
        a=x
        b=y
    else:
        b=x
        a=y
    temp2=a
    while True:
        print "1"
        while temp2 > b:
            temp2 = a-b
            print "2"
            
        temp=temp2
        a=b
        b=temp
        temp2=a
        print "4"
        if temp==0:
            print "3"
            break
        
    return a
print findGcd(24,5)
