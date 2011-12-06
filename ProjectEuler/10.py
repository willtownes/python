'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

def digits(m):
    '''converts a positive integer m into a list of its digits'''
    ms = str(m)
    digs = []
    for i in ms:
        digs.append(int(i))
    return digs
        
def listprimes(m):
    '''returns a list of all prime numbers smaller than m'''
    primes = [2]
    counter = 3
    isprime = True #flags whether counter is prime or not
    while primes[-1]<m:
        isprime = True
        for k in primes:
            if counter%k == 0:
                isprime = False
                break #if counter number is evenly divisible by any preceding prime, it is not prime.
            else:
                pass
        if isprime: #implies the previous loop ran through whole list of primes and found counter to be nondivisible by each of them.
            primes.append(counter)
        else:
            pass
        counter+=2 #performance improvement - only odd numbers can be primes.
    primes.remove(primes[-1]) #last item in list is greater than m, so remove it.
    return primes

### simpler, but possibly slower version of listprimes 
##        elif True in [counter%k == 0 for k in primes]: #rate limiting (SLOW) step!
##            pass #if counter number is evenly divisible by any preceding prime, it is not prime.
##        else:
##            primes.append(counter)

def listprimes2(m):
    '''another attempt to list all primes below m'''
    values = range(m+1) #note that in this list the key and the value are the same.
    primes = values[:]
    primes[1] = 0 #1 doesn't count as a prime
    for i in values:
        if primes[i] == 0:
            pass
        else:
            for j in values[i+1:]:
                if primes[j]==0 or primes[j]%i != 0:
                    pass
                else:
                    primes[j] = 0
    return primes

    
import time
tstart = time.time()
ans = sum(listprimes2(2000000))
telapsed = time.time()-tstart
