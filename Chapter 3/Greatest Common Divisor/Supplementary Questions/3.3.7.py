import math
def findscm(x,y):
    scm=1
    if x%2==0 and y%2==0:
        scm=2
    else:
        if x>y:
            a=x
            b=y
        else:
            a=y
            b=x

        if a%b==0:
            scm=b
            
            
        for i in range(3,int(math.sqrt(b)),2):
            if a%i==0 and b%i==0:
                scm=i
                break

    return scm

print findscm(7,49)
                       
        
