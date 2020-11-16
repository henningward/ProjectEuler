import time
from fractions import Fraction
import decimal
# https://projecteuler.net/problem=57
# Square root convergents


def Main():
    lastFraction =[1, 0]
    currentFraction = [3, 2]
    i = 0
    for j in range(1000):
        temp = currentFraction[:]
        currentFraction[0] = temp[0] * 2 + lastFraction[0]
        currentFraction[1] = temp[0] + temp[1]
        lastFraction = temp
        if len(str(currentFraction[1])) < len(str(currentFraction[0])):
            i = i + 1
    return i

start_time = time.time()
result = Main()

print("--- %s seconds ---" % (time.time() - start_time))
print("----------------------------------")
print("result: " + str(result))
print("----------------------------------")
