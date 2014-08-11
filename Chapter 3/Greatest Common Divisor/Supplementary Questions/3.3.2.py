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

  



def findGcd(x,y):
    list1=listDivisor(x)
    list2=listDivisor(y)

    list3 = list(set(list1)&set(list2))
    return max(list3)

print findGcd(100,25)
