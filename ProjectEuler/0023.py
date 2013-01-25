'''
Project Euler Problem 23
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''

from euler import divisorsum
from itertools import combinations_with_replacement

def isabundant(n):
    '''returns True if the number n is abundant'''
    if divisorsum(n)>n:
        return True
    else:
        return False

def isabundantsum(n,abundants=None):
    '''returns True if the number can be represented by the sum of two abundant numbers, which can be passed in as a list to speed things up if the function needs to be called many times.'''
    if abundants==None: abundants = filter(isabundant,xrange(28123))
    if n<24:
        return False
    elif n>28123:
        return True
    else:
        cutoff = n/2
        for i in abundants:
            if i>cutoff:
                break #halfway point reached, no need to check further.
            elif n-i in abundants:
                return True #this should break out of the loop as soon as a pair of abundant numbers is found that sums to n
        return False #exhausted the list of abundant numbers without finding any matched pair that sum to n

abundants = filter(isabundant,xrange(2,28123))
abundantsums = filter(lambda x: x<=28123,sorted(set(map(sum,combinations_with_replacement(abundants,2))))) #expensive sort operation?
total = 0
for n in xrange(28123,0,-1): #check all positive integers, reverse order makes the pop() method faster
    if abundantsums == []:
        total += sum(xrange(1,n+1))
        break
    elif n==abundantsums[-1]:
        abundantsums.pop() #break off the last item since n has now gone below it
    else:
        total += n
print(total)