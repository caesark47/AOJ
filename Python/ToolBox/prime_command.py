import sys
def get_primes(n):
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in xrange(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in xrange(i ** 2, n, i):
                primes[j] = False
    return [i for i in xrange(2, n) if primes[i]]

argvs = sys.argv
if(len(argvs) > 1):
	primes = get_primes(int(argvs[1]))
	print primes
