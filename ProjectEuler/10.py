'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

def listprimes(m):
    '''another attempt to list all primes below m'''
    values = range(m+1) #note that in this list the key and the value are the same.
    primes = values[:]
    primes[1] = 0 #1 doesn't count as a prime
    sqrt = m**.5
    for i in values[:int(sqrt)+1]:
        if primes[i] == 0:
            pass
        else:
            for j in values[i+1:]:
                if primes[j]==0 or primes[j]%i != 0:
                    pass
                else:
                    primes[j] = 0
    return list(set(primes)) #get rid of all those zeroes!

import time
tstart = time.time()
ans = sum(listprimes(2000000))
telapsed = time.time()-tstart
print(ans)

