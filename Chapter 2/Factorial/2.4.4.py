def fac_largestfactor(n):
    factor=1
    for i in range(1,n+1):
        if(n%i==0):
           factor=i
        else:
            break
           
    return factor

print fac_largestfactor(120)
