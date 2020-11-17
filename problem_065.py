import time
import math
# https://projecteuler.net/problem=65
# Triangular, pentagonal, and hexagonal

def Main():
    a = 1457
    b = 1264
    temp = 0
    for i in range(88):
        temp = a 
        a = a + b
        b = temp
    return sum([int(n) for n in str(a)])


start_time = time.time()
result = Main()

print("--- %s seconds ---" % (time.time() - start_time))
print("------------------------------------")
print("result: " + str(result))
print("------------------------------------")
