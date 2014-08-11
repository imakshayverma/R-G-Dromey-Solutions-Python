def fac_check(n):
    product=1
    for i in range(1,n+1):
        product= product* i
        if(n%i==0):
            if (product == n):
                print str(n)+ " is a Factorial Number"
                break
            else:
                continue
        else:
            print str(n) + " is not a factorial Number"
            break
            


fac_check(121)
