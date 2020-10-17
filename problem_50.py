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

# https://projecteuler.net/problem=50
# Consecutive prime sum
def problem50():
    primes = [2, 3]
    #print(IsPrime(primes, 1000))
    total = 2
    iter = 0
    while primes[-1] < 1000000:
        iter = iter + 1
        i = 6 * iter - 1
        if IsPrime(primes, i):
            primes.append(i)
            total = total + 1
            #print(primes[-1])

        i = 6 * iter + 1
        if IsPrime(primes, i):
            primes.append(i)
            total = total + 1
            #print(primes[-1])

    #print(primes)
    primesum = 0
    bestCon = 0

    primecopy = primes
    addj = 2
    tempaddj = 0

    lastprime = primecopy[-1]
    primesumcopy = primecopy[:]
    primeaddjs = []


    bestCon = 0

    iterat = 0
    while primecopy:

        lastprime = primecopy[-1]

        ind = bisect.bisect_left(primecopy, lastprime/addj*3)
        primesumcopy = primecopy[:ind]
        primeaddjs = []
        primesum = 0

        while primesumcopy:

            primeaddjs = []
            primesum = 0
            tempaddj = 0
            #print(primesumcopy[:3:-1])
            for currentprime in primesumcopy[::-1]:
                primesum = primesum + currentprime
                tempaddj = tempaddj + 1
                primeaddjs.append(currentprime)

                if primesum > lastprime:
                    break
                if primesum == lastprime:
                    if addj < tempaddj:
                        print("jaddaaa. Addj: ", tempaddj)
                        print("vi traff paa ", primesum)
                        print("primes: ", primeaddjs)
                        addj = tempaddj
                        tempaddj = 0

            primesumcopy.pop()
            primesum = 0
            tempaddj = 0

        primecopy.pop()

problem50()