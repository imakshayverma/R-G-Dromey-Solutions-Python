def listDivisor(m):
    limit = m
    list = []
    i=1
    while i < limit:
        
        if m%i==0:
            
            list.extend([i, m/i])
            limit = m/i
        i=i+1
    list.sort()
    return list

maxNumber=0
maxDivisor =0
for i in range(1,100):

    if maxDivisor<len(listDivisor(i)):
        maxDivisor=len(listDivisor(i))
        maxNumber = i
        
print maxNumber
