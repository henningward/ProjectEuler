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



def problem3():

    primes = [2, 3, 5]
    i = 3
    thePrime = 600851475143

    def searchForPrimeFactors(limit):
        for i in range(limit):
            i = i+1
            if IsPrime(primes, i):
                primes.append(i)
        thePrime = 600851475143
        largestPrime = 0
        for prime in primes[::-1]:
            if thePrime % prime == 0:
                if largestPrime == 0:
                    largestPrime = prime
                thePrime =  thePrime / prime
        return thePrime, largestPrime
        
    factr = 1
    while thePrime > 1:
        factr = factr * 5
        thePrime, largestPrime = searchForPrimeFactors(factr)
        if thePrime == 1:
            print "largest prime factor:", largestPrime

problem3()