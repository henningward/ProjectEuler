import time

# https://projecteuler.net/problem=21
# Amicable numbers

def DivisorSums(num):
    divisorSum = 0

    for i in range(1, int(num/2) + 1):
        if num % i == 0:
            divisorSum = divisorSum + i
    return divisorSum

def problem21():
    res = 0
    for i in range(1, 10001):
        a = DivisorSums(i)
        b = DivisorSums(a)
        if (i == b and not i == a):
            res = res + a 
    print("antall findings: " + str(res))


start_time = time.time()
problem21()
print("--- %s seconds ---" % (time.time() - start_time))

