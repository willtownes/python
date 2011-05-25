print "AHOY! I'm the Dread Pirate Roberts, and I have a secret!"
print "It is a number from 1 to 99. I'll give you 6 tries. "

import random
secret = random.randint(1,100)
guess = 0
tries = 0

while guess != secret and tries < 6:
    guess = input("what's yer guess? ")
    if guess < secret:
        print "Too low, ye scurvy dog!"
    elif guess > secret:
        print "Too high, landlubber!"
    elif guess == secret:
        print "Avast, found my secret, ye did!"
        import sys
        sys.exit()
    else:
        print "YARR, that doesn't make sense!"
    tries = tries + 1
  
print "no more guesses! Better luck next time, matey."
print "the secret number was", secret
