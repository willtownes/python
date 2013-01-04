'''
Project Euler Problem 27
'''

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
    
def nprimes(a,b):
    '''for n=0,1,2,..; calculates the number of consecutive primes in the sequence {n^2+a*n+b}'''
    n=0
    val=b
    while isprime(val):
        n+=1
        val=n**2+a*n+b
    return n
    
if __name__=="__main__":
    maxprimes=0
    for a in xrange(-999,1000):
        for b in xrange(-999,1000):
            current=nprimes(a,b)
            if current>maxprimes: a_best,b_best,maxprimes=a,b,current
    print("a_best= %d. b_best= %d. maxprimes= %d."%(a_best,b_best,maxprimes))
    print("answer: %d"%(a_best*b_best))