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

print listDivisor(2376)  
