'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''

#First, decide how many digits are allowed in the RHS. Only a 4-digit RHS is possible. Based on that, what combinations of LHS splits between the x are possible? 

import itertools

def filterDigits(digits):
    '''takes the digits (a string, eg "123456789") and if either of the two expressions ("1*2345==6789" and "12*345==6789") based on the 1/4/4 and 2/3/4 splits are true, then returns the right-hand side of the expression, otherwise, returns None'''
    rhs = digits[5:]
    if eval(digits[:2]+'*'+digits[2:5]+'=='+rhs) or eval(digits[:1]+'*'+digits[1:5]+'=='+rhs):
        return rhs
    else:
        return None
    

if __name__=="__main__":
    res = set([])
    for d in itertools.permutations('123456789'):
        val = filterDigits(''.join(d))
        if val: res.add(int(val))
    print(sum(res))