#Project Euler Problem 1
'''If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

mults3 = range(3,1000,3)
mults5 = range(5,1000,5)
ans = sum(set(mults3+mults5))
print(str(ans))


