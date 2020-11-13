import time

# https://projecteuler.net/problem=47
# Distinct primes factors

def IsPrime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True

def Nufactors(n, goal, primes):
    result = 0
    for prime in primes:
        if n%prime == 0:
            result = result + 1
        if result == goal:
            return result
    return result

def problem47():
    primes = []
    rrange = 100000

    for i in range(2, int(rrange/100)):
        if IsPrime(i):
            primes.append(i)
    goal = 4
    current = 0
    for i in range(1000000):
        if Nufactors(i, goal, primes) >= goal:
            current = current + 1
        else:
            current = 0
        if current == goal:
            return i - 3
    return 0



start_time = time.time()
result = problem47()

print("--- %s seconds ---" % (time.time() - start_time))
print("----------------------------------")
print("result: " + str(result))
print("----------------------------------")
