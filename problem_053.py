import time

# https://projecteuler.net/problem=53
# Combinatoric selections

def Fact(n): 
    res = 1
    for i in range(1, n+1):
        res = res * i
    return res
      
def combinatoric(n, r):
    return Fact(n) / (Fact(r) * Fact(n-r))

def problem53():
    res = 0
    print(combinatoric(5,3))
    for r in range(1, 100):
        for n in range(r+1, 101):
            if combinatoric(n, r) > 1000000:
                res = res + 1

    return res




start_time = time.time()
result = problem53()

print("--- %s seconds ---" % (time.time() - start_time))
print("----------------------------------")
print("result: " + str(result))
print("----------------------------------")

