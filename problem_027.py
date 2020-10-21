import time

# https://projecteuler.net/problem=27
# Quadratic primes

def IsPrime(number):

    newPrime = True
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True


def ConsPrimesFromQuadraticEuler(a, b):
	for n in range(100):
		number = n**2 + a*n + b 
		if number < 0:
			return n-1
		if not (IsPrime(number)):
			return n-1
	return 0

def problem27():
	alim = 1001
	blim = 1001
	record = 0
	arec = 0
	brec = 0
	for a in range(-alim, alim):
		for b in range(-blim, blim):
			if (ConsPrimesFromQuadraticEuler(a, b)) > record:
				record = (ConsPrimesFromQuadraticEuler(a, b))
				arec = a
				brec = b
	print(record)
	print(arec*brec)

start_time = time.time()
problem27()
print("--- %s seconds ---" % (time.time() - start_time))

