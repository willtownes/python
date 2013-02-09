'''
Functions used to solve various Project Euler problems.
'''
def divisorsum(n):
    '''returns the sum of all the proper divisors of n'''
    n = float(n)
    val = 2
    total = 1
    sqroot = n**0.5
    while val < sqroot:
        if n%val == 0:
            total += sum([val,n/val])
        val += 1
    if val == sqroot: #case of where n is a perfect square, we only add it once.
        total += val
    return int(total)

def amicables(n):
    '''returns the set of all amicable pairs less than n'''
    amicable = set()
    notamicable = set()
    for i in xrange(1,n):
        if i in notamicable or i in amicable: pass
        else:
            dsum = divisorsum(i)
            if i == divisorsum(dsum) and i != dsum:
                amicable = amicable.union(set([i,dsum]))
            else:
                notamicable = notamicable.union(set([i,dsum]))
    return amicable