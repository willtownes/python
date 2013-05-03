'''
Project Euler Problem 28
What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
'''
def numberspiral(S):
    '''returns the sum of the diagonals of a number spiral matrix with side length S'''
    # important quantities:
    n = 1 # current number it jumps ahead by s-1 each time.
    N = S*S #max value of n
    k = 4 # current corner position. When this reaches 4, we need to update the side length by 2.
    total = 1 # cumulative sum
    s = 1 # current side length. The "skip" interval is s-1
    while n < N :
        if k==4: #case where all four corners have been reached 
            s+=2 #increase the side length
            k=1 #reset corner  marker to 1
        else: #case where not all corners have been visited in the layer
            k+=1 #increment corner by 1
        n += s-1 #increment number
        #print(n) #debugging
        total += n #increment total
    return total

if __name__ == "__main__":
    print(numberspiral(1001))