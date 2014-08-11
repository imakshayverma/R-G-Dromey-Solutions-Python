

def squareroot(m):
    g2=m/2
    g1=m/3
    error=0.0001
    while abs(g1-g2) >error:
        g1=g2
        g2=float((g1+(m/g2)))/2

    return g2



def SmallestDivisor(n):
    smallest_integer =1
    if n%2==0:
        smallest_integer = 2
    else:
        i=3
        while i <= int(squareroot(n)):
            if n%i == 0 :
                smallest_integer = i
               
                break
            else:
                i=i+2
               

    return smallest_integer

print SmallestDivisor(125)

        
