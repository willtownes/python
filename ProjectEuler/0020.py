'''Find the sum of the digits in the number 100!'''
import math
print(sum([int(i) for i in str(math.factorial(100))]))
