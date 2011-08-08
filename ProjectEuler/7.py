'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''

def listprimes(n):
    '''returns a list of the first n prime numbers'''
    primes = [2]
    counter = 3
    while len(primes)<n:
        if True in [counter%k == 0 for k in primes]: #if counter number is evenly divisible by any preceding prime, it is not prime.
            pass
        else:
            primes.append(counter)
        counter+=1
    return primes

ans = listprimes(10001)[-1]
