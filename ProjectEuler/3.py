'''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?'''
import math

def factor(n):
    '''builds a list of all integer factors (not necessarily prime).
    Note that if len(factor(n)) = 0, then n is prime.'''
    n = float(n)
    factors = [] #composite factors
    for i in range(2,int(math.ceil(n**.5)+1)):
        j = n/i
        if j%1 != 0: #in this case, neither i nor j are factors
            pass
        elif j in factors:
            pass
        else:
            factors.append(i)
            factors.append(int(j))
#    factors.sort() #sort list in ascending order.
    return factors

def subfactor(factorlist):
    '''converts all composite factors of n into list of their subfactors'''
    f = factorlist[:]
    for i in range(len(factorlist)): #go through list of factors and replace all composite factors with their subfactors
        subfactors = factor(factorlist[i])
        if len(subfactors) != 0:
            f[i] = subfactors
    return f

def trfactor(factorlist,pfactors):
    '''remove all prime factors from factor list and put in a set pfactor. Convert factor list into normal list'''
    factors2 = factorlist[:]
    for i in factorlist:
        if type(i) != list or if i in pfactors:
            pfactors.add(i)
            factors2.remove(i)
    factorlist = []
    for i in factors2:
        factorlist.extend(i)
    factorlist = list(set(factorlist)) #remove duplicates
    return factorlist,pfactors

def pfactor(n):
    '''returns a set of all prime factors of n'''
    p = set([1])
    f = factor(n)
    f = subfactor(f)
    while len(f) > 1:
        (f,p) = trfactor(f,p)
        f = subfactor(f)
    return p
