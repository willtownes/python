'''
The fraction is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that , which is correct, is obtained by cancelling the

s.

We shall consider fractions like,

, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''

from itertools import product
from math import gcd

res = []

def checker(nn,dd,pos=0):
    """
    nn is (num0, num1) digits. dd is (denom0, denom1) digits. 
    Pos is denom digit that is also found in numerator. 
    """
    n = 10*nn[0]+nn[1]
    d = 10*dd[0]+dd[1]
    if pos==0:
        return dd[1]*n == d*nn[0]
    elif pos==1:
        return dd[0]*n == d*nn[1]
    else:
        raise ValueError("pos must be 0 or 1")
# test:
# checker((4,9),(9,8),pos=0) is True

if __name__=="__main__":
    for dd in product(range(1,10),repeat=2): #(denom digit 1, denom digit 2) all possible
        #(excludes any number that has a zero digit).
        #we can ignore cases like (x,y)/(x,z) and (x,y)/(z,y) and zeros
        # d = dd[0]*10+dd[1] #the actual denominator
        if dd[0]>dd[1]: #left denom digit larger than right denom digit
            #case where left denom digit is on numerator's right digit
            for n0 in range(1,dd[0]):
                nn = (n0,dd[0])
                if checker(nn,dd,pos=0): res.append((nn,dd))
            #case where right denom digit is on numerator's left digit
            for n1 in range(1,10):
                nn = (dd[1],n1)
                if checker(nn,dd,pos=1): res.append((nn,dd))
        elif dd[0]<dd[1]:
            for n0 in range(1,dd[0]+1):
                nn = (n0,dd[0])
                if checker(nn,dd,pos=0): res.append((nn,dd))
        else: #dd[0]==dd[1]
            for n0 in range(1,dd[0]):
                nn = (n0,dd[0])
                if checker(nn,dd,pos=0): res.append((nn,dd))
            for n1 in range(1,dd[1]):
                nn = (dd[1],n1)
                if checker(nn,dd,pos=1): res.append((nn,dd))
    frac = [1,1]
    for n,d in res:
        frac[0]*= 10*n[0]+n[1]
        frac[1]*= 10*d[0]+d[1]
    print(frac[1]//gcd(*frac))
    