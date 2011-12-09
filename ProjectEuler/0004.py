'''
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''
import math

def ispalindrome(x):
    '''returns true if x is a palindrome, false otherwise. x must be a positive integer.'''
    match = []
    for k in range(0,len(str(x))/2): #note that integer division always rounds down.
        if str(x)[k] == str(x)[-k-1]:
            match.append(1) #build list of all digit comparisons.
        else:
            match.append(0)
    if sum(match) == len(match): #case where all digit comparisons matched up.
        ans = True
    else: #case where at least one digit comparison did not match
        ans = False
    return ans
    
palindromes = []
for i in range(1,1000):
    for j in range(1,1000):
        s = 1000-i
        t = 1000-j
        prod = s*t
        #make sure the product is an integer and that it is a palindrome.
        if prod%1==0 and ispalindrome(prod):
            palindromes.append(prod)
        else:
            pass
ans = max(palindromes)



