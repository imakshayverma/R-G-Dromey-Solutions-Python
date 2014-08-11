def squareroot(m):
    g2=m/2
    g1=m/g2
    error=0.0001
    i=0
    while abs(g1-g2) >error:
        print i
        i=i+1
        g1=g2
        g2=float((g1+(m/g2)))/2

    return g2

print squareroot(15)
