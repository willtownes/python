"""
To profile your machine's parallel capabilities, call this script with
>>> python test_parallel.py [max_processes]
where max_processes is an integer (typically something like 2-8).
"""
import multiprocessing as mp
from math import factorial
from time import time
from sys import argv

if __name__=="__main__":

    try: maxp = int(argv[1]) #user-supplied value from command line
    except IndexError: maxp = 4 #default value

    for nprocess in xrange(1,maxp+1):
        pool = mp.Pool(processes=nprocess)
        tic = time()
        results = pool.map_async(factorial, xrange(2000,4000))
        output = results.get()
        toc = time()-tic
        print("Number of processes: %d. Elapsed time: %f seconds"%(nprocess,toc))

        # Output on my machine, which has two cores (I know, it's old!)
        # Number of processes: 1. Elapsed time: 9.761838 seconds
        # Number of processes: 2. Elapsed time: 5.428259 seconds
        # Number of processes: 3. Elapsed time: 5.124158 seconds
        # Number of processes: 4. Elapsed time: 5.434701 seconds