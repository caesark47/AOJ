import math
def get_primes(goal):
	n_list = range(3,goal+1,2)
	primes = [2]
	sieve = map(lambda n:[n,1],n_list)#Sieve of Eratosthenes
	while sieve[0][0] < math.sqrt(goal):
		target = sieve[0][0]
		primes = primes + [target]
		i = 0
		while i < len(sieve):
			sieve[i][1] = 0
			i += target
		while  sieve[0][1] == 0:
			sieve = sieve[1:]
	primes = primes + map(lambda x:x[0],filter(lambda n:n[1] ,sieve))
	return primes


primes = get_primes(100000)
print primes