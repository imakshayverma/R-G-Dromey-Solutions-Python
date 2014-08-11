def factorial(n):
    product=1
    for i in range(1,n+1):
        product=product* i
    return product

def coeff_binomialTheorem(r,n):
    result=(1.0*factorial(n))/(factorial(r) *factorial(n-r))
    return result

print coeff_binomialTheorem(4,6)
