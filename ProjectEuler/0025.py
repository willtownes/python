'''
What is the first term in the Fibonacci sequence to contain 1000 digits?
'''

def fib():
    '''returns a generator that yields fibonacci tuples (index,value[-2],value[-1]).
    index tells how many items into the sequence it has progressed'''
    f1,f2 = 1,1
    while True:
        yield f1,f2
        f1,f2 = f2,(f1+f2)

if __name__ == "__main__":
    #self test code
    print("Here are the first 12 fibonacci numbers:")
    fibtest = fib() #generator object
    for i in xrange(1,13):
        print("F%d = %d"%(i,next(fibtest)[0]))
    #getting the answer code
    index = 0
    fib = fib()
    while True:
        index += 1
        val = next(fib)[0]
        if len(str(val)) >= 1000:
            break
        else: pass
    print("The first term in the Fibonacci sequence to contain 1000 digits is:")
    print(index)
    
