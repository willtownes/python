'''
Project Euler Problem 243
Find the smallest denominator with a resilience below the threshold
'''
from fractions import gcd
from fractions import Fraction as frac
import math

def resilience0(d): #works, but is too slow. I think this is using "Euclid's Algorithm" for gcd function, which seems to be the rate limiting step.
    '''return the resilience of the denominator d. This is the ratio of proper fractions with n as denominator that cannot be cancelled down'''
    counter=0
    for num in xrange(1,d):
        if gcd(num,d)==1: counter+=1
        else: pass
    return counter/float(d-1)

def isprime(x):
    '''returns True if the number is prime, otherwise, False'''
    if x<2: 
        #print('Non-prime, non-composite number %d encountered!'%x)
        return False #numbers that are neither prime nor composite
    y=2
    thresh=x**.5
    res=True #if x=2, default is to return that it is prime.
    while y<=thresh:
        if x%y==0: 
            res=False
            break
        else: y+=1
    return res

def factor(n):
    '''builds a list of all integer factors (not necessarily prime).
    Note that if len(factor(n)) = 2, then n is prime.'''
    n = float(n)
    factors = [1,n] #composite factors
    for i in xrange(2,int(math.ceil(n**.5)+1)):
        j = n/i
        if j%1 != 0: #in this case, neither i nor j are factors
            pass
        elif j in factors:
            pass
        else:
            factors.append(i)
            factors.append(int(j))
#    factors.sort() #sort list in ascending order.
    return factors
    
def eulerphi(d):
    '''return euler's phi for the input'''
    factors=factor(d)
    primes=(f for f in factors if isprime(f)) #generator expression
    invprimes=map(lambda x: frac(x-1,x),primes)
    phi=d*reduce(lambda x,y: x*y,invprimes) #formula from http://en.wikipedia.org/wiki/Euler%27s_totient_function
    return phi
    
def resilience(d):
    '''faster way to find all resilient fractions by using Euler's Totient (Phi)'''
    return eulerphi(d)/float(d-1)

if __name__ == "__main__":
    d=3
    r=resilience(d)
    thresh=15499./94744
    #thresh=4./10
    while r >= thresh:
        d+=1 #fast ramp up to waste less time on low values
        r=resilience(d)
    print(d)
    #r is now too far below the threshold. Slowly decrease d until threshold is reached.
    #print('upper limit reached, now descending')
    #while r < thresh:
    #    d_old= d
    #    d-=1
    #    r=resilience(d)
    #print(d_old)