'''
In England the currency is made up of pound, L, and pence, p, and there are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, L1 (100p) and L2 (200p).

It is possible to make L2 in the following way:

    1xL1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p

How many different ways can L2 be made using any number of coins?
'''

COINS = (1,2,5,10,20,50,100,200)

def coinSum(n,k):
    '''return the number of ways to have a sum n using the first k coins from COINS'''
    # Algorithm is from: http://andrew.neitsch.ca/publications/m496pres1.nb.pdf
    if k>len(COINS)-1 or n < 0:
        return 0
    elif n==0:
        return 1
    else:
        return coinSum(n,k+1) + coinSum(n-COINS[k],k)

if __name__=="__main__":
    print(coinSum(200,0))
            
        
#sum, ways
#1, 1
#2, 2
#3, 2
#4, 3
#5, 4