# https://projecteuler.net/problem=7
# primtall nummer 100001
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

def problem7():
    primes = [2, 3, 5]
    print(IsPrime(primes, 11))
    i = 3
    while len(primes) < 10002:
        i = i+1
        if IsPrime(primes, i):
            primes.append(i)
            print(len(primes))
    #print(primes)
    print(len(primes))
    print("primtall nummer 10001 er", primes[10000])

problem7()