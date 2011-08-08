'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
x = [2**4,3**2,5,7,11,13,17,19]
ans = reduce(lambda x,y: x*y,x)
