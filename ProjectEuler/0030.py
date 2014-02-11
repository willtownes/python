'''
Project Euler Problem 30
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.
The sum of these numbers is 1634 + 8208 + 9474 = 19316.
Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''

powers4 = dict((str(x),x**4) for x in xrange(10))
powers5 = dict((str(x),x**5) for x in xrange(10))

def isSumFifthPowers(number):
    '''Returns True if the sum of the fifth powers of the digits in the number equals the number, False otherwise'''
    numstr=str(number)
    digitSum=0
    for char in numstr:
        digitSum += powers5[char]
        if digitSum > number:
            return False
    if digitSum == number:
        return True
    else:
        return False
    
if __name__ == "__main__":
    res = []
    for i in xrange(10,1000000):
        if isSumFifthPowers(i):
            res.append(i)
    print(sum(res))