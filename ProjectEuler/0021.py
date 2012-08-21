'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.
For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
Evaluate the sum of all the amicable numbers under 10000.
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

if __name__ == "__main__":
    print("Divisor of 220 should be 284, we find it to be %d"%divisorsum(220))
    print("Divisor of 284 should be 220, we find it to be %d"%divisorsum(284))
    maxval = 10000   
    print("The sum of all the amicable pairs less than %d is:"%maxval)
    print(sum(amicables(maxval)))
        
