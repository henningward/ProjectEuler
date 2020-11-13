import time
import math
# https://projecteuler.net/problem=39
# Integer right triangles

def Problem39():

    solutions = [0] * 1000

    for a in range(999):
        for b in range(999):
            c = math.sqrt(a**2 + b**2)
            if a + b + c > 1000:
                continue
            elif c.is_integer():
                #print(c)
                solutions[int(a+b+c-1)] += 1


    index = 0
    res = 0
    for i in range(len(solutions)):
        if solutions[i] > res:
            res = solutions[i]
            index = i + 1
    print(index)

start_time = time.time()
Problem39()
print("--- %s seconds ---" % (time.time() - start_time))