import time
from itertools import groupby

# https://projecteuler.net/problem=55
# Lychrel numbers


def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)

def IsPalindrome(n): return all_equal([n, int(str(n)[::-1])])

def IsNotLychrel(n, itr):
    nreversed = int(str(n)[::-1])
    r = n + nreversed
    if IsPalindrome(r):
        ,
        
    elif (itr < 50):
        return IsNotLychrel(r, itr + 1)
    else:
        return 0
    #IsLychrel(n, itr+1)

def problem55():
    i = 0
    for n in range(1, 10001):
        if IsNotLychrel(n, 1) == 0:
            i = i + 1
    return i


start_time = time.time()
result = problem55()

print("--- %s seconds ---" % (time.time() - start_time))
print("----------------------------------")
print("result: " + str(result))
print("----------------------------------")