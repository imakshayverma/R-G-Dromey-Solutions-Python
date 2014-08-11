#PRogram to calculate the sum of squares of n numbers.

def calc(l):
    sum=0
    for i in range(len(l)):
        sum=sum+(l[i] * l[i])
        

    print sum

l=[1,2,3]
calc(l)

