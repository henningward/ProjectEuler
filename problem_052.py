import time
from itertools import groupby
# https://projecteuler.net/problem=52
# Permuted multiples

def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)

def IsPermutations(llist):
    llist = [int(''.join(map(str,sorted(str(n))))) for n in llist]
    return all_equal(llist)

def problem52():

    upr = 10000000
    for n in range(1, upr):
        success = True
        for i in range(2, 7):
            if not IsPermutations([n, n*i]):
                success = False
                break
        if success:
            return n

    return (":(")



start_time = time.time()
result = problem52()

print("--- %s seconds ---" % (time.time() - start_time))
print("----------------------------------")
print("result: " + str(result))
print("----------------------------------")


