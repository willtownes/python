'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.
For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
Evaluate the sum of all the amicable numbers under 10000.
'''

from euler import divisorsum,amicables

if __name__ == "__main__":
    print("Divisor of 220 should be 284, we find it to be %d"%divisorsum(220))
    print("Divisor of 284 should be 220, we find it to be %d"%divisorsum(284))
    maxval = 10000   
    print("The sum of all the amicable pairs less than %d is:"%maxval)
    print(sum(amicables(maxval)))
        
