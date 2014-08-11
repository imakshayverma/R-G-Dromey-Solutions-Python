#PRogram to calculate the harmonic mean.
#Under Construction

def calc(l):
    denom=0
    for i in range(len(l)):
        denom=denom+(1.0/l[i])
        

    mean= len(l)/denom
    print mean

l=[1,2,3]
calc(l)

