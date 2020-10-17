# https://projecteuler.net/problem=10
# Find the sum of all the primes below two million.
def IsPrime(primes, number):

    newPrime = True
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True

    for prime in primes:
        if number%prime == 0:
            newPrime = False
    return newPrime

def problem10():
    primes = [2, 3]
    iter = 0
    primelimit = 2000000
    while primes[-1] < primelimit:

        iter = iter + 1
        i = 6 * iter - 1

        if IsPrime(primes, i):
            primes.append(i)

        i = 6 * iter + 1
        if IsPrime(primes, i):
            primes.append(i)
    while primes[-1] > primelimit:
        primes.pop()

    primesum = 0

    for prime in primes:
        primesum = primesum + prime

    print "primtallsummen for primtall under", primelimit, "er:", primesum

problem10()