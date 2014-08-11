#Program to print out n values of the sequence - 1 -1 1 -1 1 -1 ...

def sequence(n):
    
    for i in range (n):
        print (-1) ** i,

sequence(8)
