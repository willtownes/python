'''
Project Euler Problem 26
Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''
# We only need to check numbers n that are coprime to 10
# then what we need to do is compute the order of 10 mod n
# the order is the smallest integer k such that 10^k mod n = 1
# to do this , try k=1,2,... and each time divide by n. If the remainder = 1, stop. that value of k is the period of the repeating decimal.
# theoretical reference: http://mathforum.org/library/drmath/view/67018.html

def getMaxPeriod(N=1000):
    '''returns the number d<N and the period of its repeating decimal form such that the period is maximum.'''
    maxperiod=1
    d=3
    for n in xrange(3,N+1,2):
        if n % 5 == 0: continue #skip all numbers not coprime to 10
        k = 1
        while 10**k % n != 1:
            k += 1
        if k > maxperiod: 
            d = n
            maxperiod = k
    return d,maxperiod

if __name__ == "__main__":
    print(getMaxPeriod(1000)[0])