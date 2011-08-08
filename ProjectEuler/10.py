'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

def listprimes(m):
    '''returns a list of all prime numbers smaller than m'''
    primes = [2]
    counter = 3
    while primes[-1]<m:
        if True in [counter%k == 0 for k in primes]: #if counter number is evenly divisible by any preceding prime, it is not prime.
            pass
        else:
            primes.append(counter)
        counter+=1
    primes = primes[:-1]
    return primes

#ans = sum(listprimes(2000000))
#input(ans)
