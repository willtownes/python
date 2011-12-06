'''
Sample code to demonstrate parallel processing, derived from:
http://www.astrobetter.com/parallel-processing-in-python/
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

# Just replace this (calling one function twice, in series):
desired_values = [function(args) for args in [args1,args2]]
 
# ... with this (calling one function twice, in parallel):
import pprocess
nproc = 4  	# maximum number of simultaneous processes desired
results = pprocess.Map(limit=nproc, reuse=1)
parallel_function = results.manage(pprocess.MakeReusable(function))
parallel_function(args1)
parallel_function(args2)
desired_values = results[0:2]
